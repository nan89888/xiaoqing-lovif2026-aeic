# Archive coverage and retention

This repository preserves a public reproduction package. The 2026-10-23 supplement adds the recovered inference sources, native entropy-coder sources, fixed runtime configuration, current environment versions, source provenance, final-bitstream hashes and private-archive hashes.

| Material | GitHub coverage | Retention decision |
| --- | --- | --- |
| AEIC ME ft16 fp16 checkpoint | Verified `v1.0.0` Release asset | Reuse the existing upload |
| Recovered inference and C++ entropy runtime | Source files, upstream-relative patch and per-file hashes | Necessary supplement |
| Final settings and output inventory | Configuration, 100 bitstream hashes, aggregate bytes | Necessary supplement |
| Server runtime versions | JSON snapshot and inference requirements | Necessary supplement; not a July lockfile |
| Original training/validation/test images and annotations | Outside the public package | Preserve all dataset locations privately |
| Submitted bitstreams and reconstruction PNGs | Hash records only | Preserve the complete private final-result archive |
| Complete code-submission ZIPs | Filename, byte count and SHA-256 | Preserve private ZIPs; contain third-party weights and experimental branches |
| Other checkpoints and experiment trees | Outside the selected final-runtime supplement | Preserve until selected experiments have a separate archive |
| Temporary grids, caches and repeated results | Outside the supplement | Review after important private artifacts are independently backed up |
| Raw logs, contact details, server paths and original work notes | Outside the public package | Retain privately |

The full code ZIPs are roughly 3.4 and 3.5 GiB and contain third-party runtime weights and other experimental materials. This supplement follows the repository's existing model-release policy rather than uploading those complete ZIPs as public assets. Their exact hashes are recorded in `configs/private_archive_checksums.json`.

Uploading this supplement completes the selected public source recovery. It does not establish that every important server artifact is backed up to GitHub. Final result payloads, experimental checkpoints and original private archives still need independent backup before broad server cleanup. All datasets and the server originals were retained during publication.

## Research-archive supplement (2026-10-23)

The research-archive prerelease now also preserves historical training/selection/evaluation scripts, AEIC training configurations, JSON experiment records, corrected lineage/audit notes, subset membership, five selected refiner checkpoints and five codebooks from the submitted hybrid development package. See `../research-archive/README.md` and `RETENTION_DECISIONS.md` for the updated coverage and the specific unselected intermediate artifacts recommended for cleanup review. Original datasets, final payloads, complete code ZIPs and the custom pruned runtime remain private retention items.
