# Recovered AEIC inference runtime

This directory preserves 26 source/license files byte-for-byte from the active AEIC server checkout inspected on 2026-10-23. The checkout was based on upstream `ff4031b0f5826ae88d3de87e5cf5c03c995faf5e` with local modifications.

It includes the recovered `y_quant_step` implementation, Boolean argument parsing, native rANS corrections, latent-adapter compatibility and runtime loading changes. These changes reflect the active checkout; their exact relationship to the July final-test execution remains subject to verification.

See `../docs/RECOVERED_SOURCE.md` for build/run instructions and provenance. `../configs/recovered_source_manifest.json` records the original bytes and hashes. Generated binaries belong in `src/codec/` after building; they are intentionally excluded from Git.

The upstream AEIC MIT license is retained in `LICENSE`. Individual sources retain their own copyright and license notices, including Microsoft rANS code and the InterDigital entropy-model notice. Third-party model weights remain separate dependencies.
