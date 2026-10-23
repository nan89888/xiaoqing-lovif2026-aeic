import argparse

def str2bool(v):
    if isinstance(v, bool):
        return v
    if str(v).lower() in ("yes", "true", "t", "1", "y"):
        return True
    if str(v).lower() in ("no", "false", "f", "0", "n"):
        return False
    raise argparse.ArgumentTypeError("Boolean value expected.")

def parse_args_testing(input_args=None):

    parser = argparse.ArgumentParser()

    # pretrained weights
    parser.add_argument("--sd_path", required=True, help="Path to SD-Turbo")
    parser.add_argument("--codec_path", required=True, help="Path to pretrained AEIC weights")
    parser.add_argument("--vae_decoder_path", required=True, help="Path to pretrained pruned VAE decoder weights")

    # testing images
    parser.add_argument("--img_path", type=str, required=True, default='/data/Kodak/')

    # output path
    parser.add_argument("--rec_path", type=str, required=True, default='/output/rec/')
    parser.add_argument("--bin_path", type=str, required=True, default='/output/bin/')

    # model details
    parser.add_argument("--codec_type", type=str, required=True, default='AEIC-ME', help="The type of codec to use, should be one of ['AEIC-ME', 'AEIC-SE']")
    parser.add_argument("--lora_rank_unet", default=32, type=int)

    # testing details
    parser.add_argument("--enable_xformers_memory_efficient_attention", type=str2bool, default=True, help="Whether or not to use xformers.")
    parser.add_argument("--color_fix", type=str2bool, default=True, help="Whether or not to use color fix.")
    parser.add_argument("--use_practical_entropy_coding", default=False, action="store_true")
    parser.add_argument("--encode_only", default=False, action="store_true", help="Only write bitstreams; skip local decode/reconstruction.")
    parser.add_argument("--merge_LoRA", type=str2bool, default=True)
    parser.add_argument("--compile_model", type=str2bool, default=True)
    parser.add_argument("--big_encoder_50m", type=str2bool, default=False)
    parser.add_argument("--y_quant_step", type=float, default=1.0, help="Fixed practical y-latent quantization step. Values >1 reduce rate.")
    parser.add_argument("--use_tiled_vae", type=str2bool, default=True)
    parser.add_argument("--use_tiled_unet", type=str2bool, default=True)
    parser.add_argument("--vae_decoder_tiled_size", type=int, default=160, help="Tiled VAE decoder tile size. Switch to 128 if OOM.")
    parser.add_argument("--latent_tiled_size", type=int, default=96, help="Tiled latent tile size.")
    parser.add_argument("--latent_tiled_overlap", type=int, default=32, help="Tiled latent tile overlap.")

    if input_args is not None:
        args = parser.parse_args(input_args)
    else:
        args = parser.parse_args()

    return args
