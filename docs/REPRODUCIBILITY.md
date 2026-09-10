# Reproducibility Statement

## What this package reproduces

It reproduces the public AEIC practical-entropy-coding pipeline with the XIAOQING `ME_ft16_fp16` checkpoint when the listed third-party weights are supplied. It provides actual bitstream byte accounting for any input image directory.

## What this package records but cannot currently reproduce bit-exactly

The final LoViF test submission recorded `y_quant_step=1.13`. The competition archive preserves this setting in the final submission readme, but not the corresponding local source modification. The public upstream AEIC code pinned by this repository does not have an argument or implementation for this parameter. Therefore, the public wrapper does not make a bit-exact final-test claim.

## Excluded material

- challenge validation and final-test images;
- final-test reconstructed PNG files and bitstreams;
- the 3.54 GB code-submission archive;
- unrelated RVQ, selector, refiner, and post-processing experiment branches; and
- server paths, local logs, and personal contact details.

## Path to a complete release

To make a future version bit-exact, recover the source patch implementing `y_quant_step`, write a deterministic encoder/decoder test, and verify its output against a preserved final-test bitstream using a permitted non-public audit environment. Only then update this statement and tag a new release.
