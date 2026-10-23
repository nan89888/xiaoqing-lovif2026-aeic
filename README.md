# XIAOQING at LoViF 2026 Ultra-Low Bitrate Image Compression

This repository documents the reproducible AEIC-based submission prepared by team XIAOQING for the LoViF 2026 Challenge on Ultra-Low Bitrate Image Compression at ECCV 2026.

The final-test submission used an AEIC-ME codec with the `ME_ft16_fp16` checkpoint and practical entropy coding. It was submitted under the strict 0.008 weighted-BPP budget and ranked third on the preliminary final-test leaderboard.

## Scope and status

This is a public reproduction package, not a redistribution of the official test set, reconstructed test images, or submitted bitstreams. It contains:

- the recovered AEIC inference runtime and native entropy-coder source;
- fixed recovered-runtime and original public-baseline runners;
- source/bitstream/archive checksums and observed environment versions;
- a pinned setup script for the public AEIC implementation;
- the fixed final-test configuration and checkpoint checksums;
- an audited runner for the publicly released AEIC baseline; and
- a BPP audit utility that counts the actual bytes in a directory of bitstreams.

The original competition decoder package contained the final checkpoint and dependencies. The source-recovery supplement is documented below. The official test images and its 100 submitted bitstreams are intentionally excluded.

### Source recovery update (2026-10-23)

The missing `y_quant_step=1.13` implementation was recovered from the active server checkout. This repository now preserves the inference runtime and native entropy-coder sources, source checksums, a fixed runner and observed environment versions. See [recovered-source instructions](docs/RECOVERED_SOURCE.md).

Full final-test bit-exact equivalence remains unverified. The recovered active source and the historical submitted decoder ZIP have distinct provenance. The original `v1.0.0` baseline package remains in Git history and its checkpoint Release asset is unchanged.

### Historical research archive

Training/selection/evaluation scripts, configurations, metrics and corrected audit notes are preserved in the [research archive](research-archive/README.md), alongside five selected historical refiner models and five codebooks. These development artifacts are distinct from the final pure ME-ft16 result. See [retention decisions](docs/RETENTION_DECISIONS.md) for the server-cleanup boundary.

## Final submission record

| Field | Value |
| --- | --- |
| Team | XIAOQING |
| Codec family | AEIC-ME |
| Checkpoint key | `ME_ft16_fp16` |
| Practical entropy coding | enabled |
| Color fix | disabled |
| Model compilation | disabled |
| Test-time training / updates | none |
| Recorded `y_quant_step` | 1.13 (recovered source available; exact reproduction pending) |
| Test images | 100 PNG images, not released here |
| Total bitstream bytes | 226,877 |
| Weighted BPP | 0.007921208421 |

## Quick start

The commands below reproduce the publicly released AEIC inference path. A Linux environment with a CUDA-capable GPU is expected.

```bash
git clone https://github.com/nan89888/xiaoqing-lovif2026-aeic.git
cd xiaoqing-lovif2026-aeic
bash scripts/fetch_aeic.sh
conda create -n xiaoqing-aeic python=3.10 -y
conda activate xiaoqing-aeic
pip install -r upstream-aeic/requirements.txt
```

Download the model release asset listed in [`docs/MODEL_RELEASE.md`](docs/MODEL_RELEASE.md), verify its SHA256 checksum, and extract it into `weights/`.

```bash
bash scripts/run_public_aeic_me_ft16.sh /path/to/png_inputs outputs/run
python scripts/audit_bpp.py --bitstream-dir outputs/run/bitstream
```

`run_public_aeic_me_ft16.sh` invokes the pinned public AEIC source with practical entropy coding. The recovered-source path has separate setup and validation instructions:

```bash
python -m pip install -r requirements-recovered.txt
bash scripts/build_recovered_entropy.sh
python -m unittest discover -s tests -v
bash scripts/run_recovered_aeic_me_ft16.sh /path/to/png_inputs outputs/recovered-run
```

See [archive coverage](docs/ARCHIVE_COVERAGE.md) for the public/private backup boundary.

## Repository layout

```text
recovered-aeic/          Recovered inference and C++ runtime source
patches/                 Upstream-relative source recovery patch
tests/                   CPU runtime and entropy checks
configs/                 Final/public/recovered configurations and audit manifests
docs/                    Release, provenance, and reproducibility notes
scripts/                 Setup, execution, and rate-audit tools
weights/                 Empty after clone; populate from a GitHub Release asset
upstream-aeic/           Created locally by scripts/fetch_aeic.sh; ignored by Git
```

## Data and model provenance

- AEIC source: [LuizScarlet/AEIC](https://github.com/LuizScarlet/AEIC), MIT license, pinned in `configs/upstream_aeic.json`.
- SD-Turbo weights: [stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo), subject to its own model license.
- Pruned VAE decoder: [Guaishou74851/AdcSR](https://huggingface.co/Guaishou74851/AdcSR), subject to its own model license.
- The AEIC `ME_ft16_fp16` checkpoint is released separately as a GitHub Release asset. See [`docs/MODEL_RELEASE.md`](docs/MODEL_RELEASE.md).

The LoViF challenge data, final-test images, submitted reconstruction PNGs, and submitted bitstreams are not redistributed in this repository.

## Citation

If this package is useful, please cite the upstream AEIC work and the associated LoViF 2026 challenge report. The challenge-report bibliographic record will be added here when it is published.

## License

The XIAOQING wrapper scripts and documentation are released under the MIT License. Upstream source code, model weights, and datasets remain governed by their respective licenses.
