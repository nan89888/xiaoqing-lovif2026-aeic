# Reproducibility statement

## Available paths

The original public-baseline runner uses the pinned public upstream AEIC source and the released ME ft16 fp16 checkpoint. The 2026-10-23 supplement adds a separate recovered runtime containing the `y_quant_step=1.13` implementation, native entropy-coder changes and associated loading/argument fixes. See `RECOVERED_SOURCE.md` for instructions.

## Final-test equivalence

The final-test record specifies `y_quant_step=1.13`, 100 images, 226,877 bitstream bytes and weighted BPP 0.007921208421. The corresponding source implementation was recovered from the active server checkout on 2026-10-23 and is now preserved with per-file hashes.

This resolves the source-availability gap described by the original `v1.0.0` release. Full final-test bit-exact equivalence is still unverified. The recovered active checkout and the July 11 submitted decoder ZIP have distinct provenance. An end-to-end GPU run must be compared against the archived final bitstreams and reconstructed images before claiming exact reproduction or an official score.

## Included audit records

- recovered source bytes, hashes and upstream-relative patch;
- recorded runtime configuration and observed package versions;
- CPU argument, latent-quantization and native-entropy tests;
- checksum-only inventory of the 100 final bitstreams; and
- hashes and sizes of the original private ZIPs.

## Private retention

Official challenge images, submitted payloads, reconstruction images, full decoder ZIPs, unrelated experimental checkpoints and raw personal/server notes remain privately retained. See `ARCHIVE_COVERAGE.md` for the backup boundary and remaining retention work.
