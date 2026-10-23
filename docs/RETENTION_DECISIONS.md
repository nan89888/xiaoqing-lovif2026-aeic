# Retention decisions after research preservation

## Preserve originals privately

- Every original dataset, image and annotation, including `data_test/` and shared training/validation datasets.
- Both original code-submission ZIPs under `code_submission_packages/`, with the recorded checksums.
- The complete final-test submission directory/ZIP/report under `final_test_submissions/`.
- Historical development submission ZIPs directly under `submissions/` and the current hybrid development ZIP/report under `tmp/`.
- The custom `models/sd-turbo-pruned-aeic-fp16/` runtime until its regeneration has been independently verified.

These original submission artifacts are kept privately because the public package contains source/metadata and selected owned model artifacts rather than all image payloads and third-party runtime weights.

## Publicly archived

The final ME-ft16 checkpoint is in v1.0.0. The recovered inference/native source is in v1.1.0-recovered-source. The training/experimental source, configurations, metrics, lineage/audit records, subset membership, five selected refiners and five codebooks are in v1.2.0-research-archive.

## Recommended cleanup candidates after review

- Generated development grids, reconstructed images, candidate streams and caches under `outputs/`, once the research archive has been downloaded and verified.
- Unselected experimental training checkpoints under `outputs/`: not required by the final test; exact continuation from those snapshots is intentionally given up if they are deleted.
- Temporary experimental files under `tmp/`, excluding the retained current-hybrid result ZIP/report; all subset memberships are archived while their original dataset targets remain protected.
- Expanded duplicate code packages under `code_submission_packages/`, while preserving the ZIPs. Original differences in the fallback README/size reports are included in the research records.
- Unpacked historical development submissions and rejected diagnostic payloads, while preserving the selected private originals described above.
- Non-final evaluation variants under `final_test_runs/`, whose final canonical output remains retained under `final_test_submissions/`.
- Superseded `decoder_package_draft/`, generated logs and build/download caches, after source/configuration/metric coverage is confirmed.

The separate local cleanup manifest gives exact paths, exceptions and review status. Publishing these archives does not authorize automatic deletion, nor does it turn all remaining server files into disposable data. No server deletion was performed during this preservation task.
