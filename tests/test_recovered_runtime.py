"""CPU checks for recovered argument handling, quantization and native rANS."""
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "recovered-aeic"), str(ROOT / "recovered-aeic/src")]

from my_utils.testing_utils import parse_args_testing


class ArgumentTests(unittest.TestCase):
    def test_false_flags_and_recorded_quantization(self):
        args = parse_args_testing([
            "--sd_path", "weights", "--codec_path", "checkpoint.pkl",
            "--vae_decoder_path", "decoder.ckpt", "--img_path", "inputs",
            "--rec_path", "rec", "--bin_path", "bin", "--codec_type", "AEIC-ME",
            "--y_quant_step", "1.13", "--color_fix", "False", "--compile_model", "False",
        ])
        self.assertEqual(args.y_quant_step, 1.13)
        self.assertFalse(args.color_fix)
        self.assertFalse(args.compile_model)


class QuantizationTests(unittest.TestCase):
    def test_group_symbols_scales_and_reconstructed_latents(self):
        import numpy as np
        import torch
        from src.codec.codec_practical import PixelCodec, SCALES_MIN, SCALES_MAX, SCALES_LEVELS

        # Exercise the recovered group methods without allocating a model or GPU.
        codec = PixelCodec.__new__(PixelCodec)
        torch.nn.Module.__init__(codec)
        codec.masks = {}
        codec.my_log_scale_min = math.log(SCALES_MIN)
        codec.my_log_scale_step = (math.log(SCALES_MAX) - math.log(SCALES_MIN)) / (SCALES_LEVELS - 1)
        codec.y_cdf_group_index = 0
        means = torch.full((1, 4, 2, 2), 0.375)
        scales = torch.full_like(means, 1.7)
        latent = torch.arange(16, dtype=torch.float32).reshape(1, 4, 2, 2) / 3 - 2
        masks = codec.get_mask_four_parts(1, 4, 2, 2, device="cpu")

        for q in (1.0, 1.13, 1.5):
            codec.y_quant_step = q
            for mask in masks:
                symbols = torch.round((latent * mask - means * mask) / q)
                encoded = codec.compress_group([symbols] * 4, [scales * mask] * 4)
                expected_symbols = codec.sequeeze(symbols).flatten()
                expected_indexes = codec.my_build_indexes(codec.sequeeze(scales * mask) / q).flatten()
                np.testing.assert_array_equal(encoded[0], expected_symbols.numpy())
                np.testing.assert_array_equal(encoded[4], expected_indexes.numpy())

                class CapturedEntropy:
                    def decode_stream(self, indexes, group):
                        torch.testing.assert_close(indexes, expected_indexes)
                        return expected_symbols.clone()

                codec.entropy_coder = CapturedEntropy()
                decoded = codec.decompress_group_with_mask(scales * mask, means * mask, mask)
                torch.testing.assert_close(decoded, (symbols * q + means * mask) * mask)


class NativeEntropyTests(unittest.TestCase):
    def test_hyperprior_then_four_context_groups(self):
        import numpy as np
        import torch
        from src.codec.base_entropy_coder import EntropyCoder

        coder = EntropyCoder(ec_thread=False, stream_part=1)
        cdf = np.array([[0, 16384, 32768, 49152, 65536]], dtype=np.int32)
        group = coder.add_cdf(cdf, np.array([5], np.int32), np.array([-1], np.int32))
        values = [np.arange(-11 + i, 19 + i, dtype=np.int16) for i in range(5)]
        indexes = [np.zeros(len(v), np.int16) for v in values]
        coder.reset()
        coder.encode_with_z4y_indexes(
            values[0], indexes[0], group,
            values[1], indexes[1], values[2], indexes[2],
            values[3], indexes[3], values[4], indexes[4], group,
        )
        coder.flush()
        coder.set_stream(coder.get_encoded_stream())
        for expected, index in zip(values, indexes):
            decoded = coder.decode_stream(torch.from_numpy(index), group)
            np.testing.assert_array_equal(decoded.numpy(), expected)

    def test_signed_symbols_escape_values_and_stream_lifetime(self):
        import gc
        import numpy as np
        import torch
        from src.codec.base_entropy_coder import EntropyCoder

        coder = EntropyCoder(ec_thread=False, stream_part=1)
        cdf = np.array([[0, 16384, 32768, 49152, 65536]], dtype=np.int32)
        group = coder.add_cdf(cdf, np.array([5], np.int32), np.array([-1], np.int32))
        symbols = np.tile(np.array([-600, -3, -1, 0, 1, 3, 600], np.int16), 128)
        indexes = np.zeros(len(symbols), np.int16)
        coder.reset()
        coder.encode_with_indexes(symbols, indexes, group)
        coder.flush()
        stream = coder.get_encoded_stream()
        coder.set_stream(stream)
        del stream
        gc.collect()
        decoded = coder.decode_stream(torch.from_numpy(indexes), group)
        np.testing.assert_array_equal(decoded.numpy(), symbols)


if __name__ == "__main__":
    unittest.main()
