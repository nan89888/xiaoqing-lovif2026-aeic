# Recovered inference source, 2026-10-23

## What was recovered

The active server AEIC checkout contains an implementation of the previously missing `y_quant_step` option. This release preserves the relevant runtime and C++ entropy-coder sources, including the accompanying changes needed to load the weights and correctly interpret Boolean arguments.

The source checkout is based on upstream commit `ff4031b0f5826ae88d3de87e5cf5c03c995faf5e`. This differs from the historical public-baseline pin in `configs/upstream_aeic.json`. Each recovered file is copied verbatim and hashed in `configs/recovered_source_manifest.json`; `patches/recovered_runtime_ff4031b.patch` records the local changes relative to that checkout. The submitted July 11 decoder ZIP is a separate artifact; this snapshot does not replace its historical identity.

## Setup

Use Linux with a CUDA-capable GPU for inference, Python 3.12, CMake, a C++17 compiler and Git. `requirements-recovered.txt` records the inference-package versions observed in the existing server environment on 2026-10-23. This is a current environment snapshot rather than a historical July lockfile. Choose a PyTorch build compatible with the host CUDA driver.

```bash
python -m pip install -r requirements-recovered.txt
bash scripts/build_recovered_entropy.sh
python scripts/verify_recovered_source.py
python -m unittest discover -s tests -v
```

The native build fetches pybind11 `v2.10.4` as specified by the recovered CMake files and places two extension modules in `recovered-aeic/src/codec/`. Rebuild for each Python/platform combination. Use CMake 3.x if a newer CMake rejects the original minimum-version declarations.

Supply the checkpoint from the existing `v1.0.0` Release plus the external SD-Turbo and pruned VAE weights documented in `WEIGHT_CHECKSUMS.md`:

```text
weights/AEIC_ME_ft16_fp16.pkl
weights/halfDecoder.ckpt
weights/sd-turbo/unet/...
weights/sd-turbo/vae/...
```

Run on your own PNG input directory, using a fresh output directory:

```bash
bash scripts/run_recovered_aeic_me_ft16.sh /path/to/png_inputs outputs/recovered-run
python scripts/audit_bpp.py --bitstream-dir outputs/recovered-run/bitstream
```

This runner uses `y_quant_step=1.13`, practical entropy coding, no color fix, no model compilation and the recorded tiling defaults. It checks output coverage because the recovered compressor may skip an image after CUDA OOM. Its fixed parameters are mirrored in `configs/recovered_aeic_me_ft16.json`. The original `run_public_aeic_me_ft16.sh` remains available as the separate historical baseline path.

## Verification scope

The release verifies source hashes, argument handling, quantization/index scaling and CPU native-entropy round trips. Full-model inference, reconstructed pixels and final-test bit-exact equivalence require a separate GPU audit against the privately retained original artifacts. All server GPUs were occupied during this recovery audit, so no new GPU inference claim is made.

The archived final-test checksum manifest can be used for that comparison when the authorized test inputs are available privately. It contains filenames, sizes and hashes only.
