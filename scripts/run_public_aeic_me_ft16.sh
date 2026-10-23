#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <png_input_dir> <output_dir>" >&2
  exit 2
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT_DIR="$(cd "$1" && pwd)"
OUTPUT_DIR="$2"
AEIC_DIR="$ROOT_DIR/upstream-aeic"
WEIGHTS="$ROOT_DIR/weights"

[[ -d "$AEIC_DIR" ]] || { echo "Run scripts/fetch_aeic.sh first." >&2; exit 1; }
[[ -f "$WEIGHTS/AEIC_ME_ft16_fp16.pkl" ]] || { echo "Missing AEIC_ME_ft16_fp16.pkl; see docs/MODEL_RELEASE.md." >&2; exit 1; }
[[ -f "$WEIGHTS/halfDecoder.ckpt" ]] || { echo "Missing halfDecoder.ckpt; see docs/WEIGHT_CHECKSUMS.md." >&2; exit 1; }
[[ -d "$WEIGHTS/sd-turbo" ]] || { echo "Missing SD-Turbo directory; see docs/WEIGHT_CHECKSUMS.md." >&2; exit 1; }

mkdir -p "$OUTPUT_DIR/reconstructed" "$OUTPUT_DIR/bitstream"
export PYTHONPATH="$AEIC_DIR:$AEIC_DIR/src${PYTHONPATH:+:$PYTHONPATH}"

python "$AEIC_DIR/src/compress.py" \
  --sd_path "$WEIGHTS/sd-turbo" \
  --codec_path "$WEIGHTS/AEIC_ME_ft16_fp16.pkl" \
  --vae_decoder_path "$WEIGHTS/halfDecoder.ckpt" \
  --img_path "$INPUT_DIR" \
  --rec_path "$OUTPUT_DIR/reconstructed" \
  --bin_path "$OUTPUT_DIR/bitstream" \
  --codec_type "AEIC-ME" \
  --use_practical_entropy_coding \
  --compile_model False \
  --enable_xformers_memory_efficient_attention False \
  --color_fix False

echo "Public AEIC run completed. Use run_recovered_aeic_me_ft16.sh for the separately recovered y_quant_step=1.13 runtime."
