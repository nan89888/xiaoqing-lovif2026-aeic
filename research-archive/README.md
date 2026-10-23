# Historical research preservation

The final test used the ME-ft16 checkpoint documented in the main README. This additional archive preserves useful development work before server cleanup. It is separate from the recovered final-runtime source and from any official challenge score claim.

Download the two assets from the [research-archive prerelease](https://github.com/nan89888/xiaoqing-lovif2026-aeic/releases/tag/v1.2.0-research-archive):

- **research-records**: training/selection/evaluation source, 27 AEIC YAML configurations, JSON experiment/lineage records, corrected historical notes, hybrid manifests and all temporary subset memberships. Local machine paths and a private network address are normalized. The internal archive manifest records original and released hashes.
- **hybrid-models**: the five selected refiners and five codebooks copied into the July hybrid code package. Every tensor value, shape and dtype was checked against the original; local metadata paths and one unused training-callback reference were normalized. `hybrid_models_manifest.json` records original and release hashes and source paths.

The full active-AEIC tracked-change patch is also preserved here, relative to upstream `ff4031b0f5826ae88d3de87e5cf5c03c995faf5e`. This extends the runtime-only patch with training changes. The complete upstream source can be obtained from https://github.com/LuizScarlet/AEIC . Upstream copyright/license notices remain in source and the archive licenses directory.

The records include unsuccessful and invalidated diagnostic experiments. GT-fitted residual outputs, unencoded postprocess corrections, zlib-wrapper probes and validation-trained branches are not valid challenge score evidence. Keep the correction/audit notes with any use of the historical tables. The hybrid decoder scaffold needs an explicit branch-specific base decoder command and has not been established as a complete standalone decoder.

The archive preserves the selected historical models, source, configurations and metrics. Unselected training snapshots, optimizer state histories and intermediate reconstructed image grids are deliberately not part of the public archive. Deleting those server copies gives up exact resumption of abandoned training runs, while retaining the final model, selected historical models and research records.

`experiment_inventory.json` inventories server output groups for review. See `../docs/RETENTION_DECISIONS.md` for the retention boundary; all original datasets and important private submission ZIPs remain retention items.
