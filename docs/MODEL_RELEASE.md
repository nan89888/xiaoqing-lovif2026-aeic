# Model Release Assets

This repository intentionally keeps all model files out of Git history. Upload the following file as a GitHub Release asset after creating the repository:

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

Before publishing this checkpoint, the team should confirm it is authorized to redistribute the derived model weight under the relevant upstream licenses. Do not upload the 3.54 GB decoder-submission ZIP as a GitHub asset: it includes unrelated experiments and exceeds the scope of this public package.
