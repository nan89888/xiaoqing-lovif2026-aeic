# Model Release Assets

The model is available as a [v1.0.0 GitHub Release asset](https://github.com/nan89888/xiaoqing-lovif2026-aeic/releases/tag/v1.0.0). Model files are kept outside Git history. The verified attachment is:

```text
xiaoqing-lovif2026-me-ft16-checkpoint-20260910.zip
```

Its expected contents and checksum are:

| File after extraction | Bytes | SHA256 |
| --- | ---: | --- |
| `AEIC_ME_ft16_fp16.pkl` | 308,186,659 | `2cab9e954c90b68dd539c72b981cf70d35b18a84ea60440fc9e793700367e927` |

Extract the archive into the repository's `weights/` directory:

```bash
unzip xiaoqing-lovif2026-me-ft16-checkpoint-20260910.zip -d weights
sha256sum weights/AEIC_ME_ft16_fp16.pkl
```

The runtime also requires SD-Turbo and `halfDecoder.ckpt`. They are third-party files and are not redistributed here. Obtain them under their original licenses from the sources linked in the main README. The known SHA256 values of the copies used in the code-submission archive are recorded in [`WEIGHT_CHECKSUMS.md`](WEIGHT_CHECKSUMS.md).

The 2026-10-23 audit downloaded this attachment and verified both its GitHub-provided ZIP digest and the extracted checkpoint checksum against the server copy. The recovered-source prerelease adds source and audit records; it reuses this existing model asset. Complete decoder-submission ZIPs remain privately retained because they also contain third-party weights and experimental branches; their checksums are recorded in `configs/private_archive_checksums.json`.
