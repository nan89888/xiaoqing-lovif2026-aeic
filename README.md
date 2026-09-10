# XIAOQING at LoViF 2026 Ultra-Low Bitrate Image Compression

This repository documents the reproducible AEIC-based submission prepared by team XIAOQING for the LoViF 2026 Challenge on Ultra-Low Bitrate Image Compression at ECCV 2026.

The final-test submission used an AEIC-ME codec with the `ME_ft16_fp16` checkpoint and practical entropy coding. It was submitted under the strict 0.008 weighted-BPP budget and ranked third on the preliminary final-test leaderboard.

## Scope and status

This is a public reproduction package, not a redistribution of the official test set, reconstructed test images, or submitted bitstreams. It contains:

- a pinned setup script for the public AEIC implementation;
- the fixed final-test configuration and checkpoint checksums;
- an audited runner for the publicly released AEIC baseline; and
- a BPP audit utility that counts the actual bytes in a directory of bitstreams.

The original competition decoder package contained the final checkpoint and dependencies. The official test images and its 100 submitted bitstreams are intentionally excluded.

### Important reproducibility limitation

The archived final-test record specifies `y_quant_step=1.13`. The local source modification that exposed this parameter was not retained in the competition archive. The pinned public upstream AEIC repository does not expose it. Consequently, this repository **does not claim bit-exact reproduction of the final-test bitstreams**. It provides a runnable, documented AEIC baseline and the exact recorded final configuration for auditing and future completion.

Do not report a new score from this repository as the official challenge result. A future release can become bit-exact only after the missing source change is recovered and independently verified against the archived decoder and bitstreams.

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
| Recorded `y_quant_step` | 1.13 (source change unavailable; see limitation above) |
| Test images | 100 PNG images, not released here |
| Total bitstream bytes | 226,877 |
| Weighted BPP | 0.007921208421 |

## Quick start

The commands below reproduce the publicly released AEIC inference path. A Linux environment with a CUDA-capable GPU is expected.

```bash
git clone https://github.com/<YOUR_GITHUB_USER>/xiaoqing-lovif2026-aeic.git
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

`run_public_aeic_me_ft16.sh` invokes the pinned public AEIC source with practical entropy coding. It deliberately does not pretend to implement the unrecovered `y_quant_step=1.13` change.

## Repository layout

```text
configs/                 Recorded final-test and public-run configurations
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
