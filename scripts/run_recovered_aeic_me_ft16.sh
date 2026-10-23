#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <png_input_dir> <output_dir>" >&2
  exit 2
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT_DIR="$(cd "$1" && pwd)"
mkdir -p "$2"
OUTPUT_DIR="$(cd "$2" && pwd)"
AEIC_DIR="$ROOT_DIR/recovered-aeic"
WEIGHTS="${WEIGHTS_DIR:-$ROOT_DIR/weights}"
PYTHON_BIN="${PYTHON_BIN:-python}"

for path in "$WEIGHTS/AEIC_ME_ft16_fp16.pkl" "$WEIGHTS/halfDecoder.ckpt"; do
  [[ -f "$path" ]] || { echo "Missing weight: $path" >&2; exit 1; }
done
[[ -d "$WEIGHTS/sd-turbo" ]] || { echo "Missing $WEIGHTS/sd-turbo" >&2; exit 1; }
WEIGHTS="$(cd "$WEIGHTS" && pwd)"

export PYTHONPATH="$AEIC_DIR:$AEIC_DIR/src${PYTHONPATH:+:$PYTHONPATH}"
"$PYTHON_BIN" "$ROOT_DIR/scripts/verify_recovered_source.py"
"$PYTHON_BIN" -c 'import src.codec.MLCodec_CXX, src.codec.MLCodec_rans' || {
  echo "Build entropy extensions with scripts/build_recovered_entropy.sh in this Python environment." >&2
  exit 1
}
mkdir -p "$OUTPUT_DIR/reconstructed" "$OUTPUT_DIR/bitstream"
cd "$AEIC_DIR"
"$PYTHON_BIN" src/compress.py \
  --sd_path "$WEIGHTS/sd-turbo" \
  --codec_path "$WEIGHTS/AEIC_ME_ft16_fp16.pkl" \
  --vae_decoder_path "$WEIGHTS/halfDecoder.ckpt" \
  --img_path "$INPUT_DIR" \
  --rec_path "$OUTPUT_DIR/reconstructed" \
  --bin_path "$OUTPUT_DIR/bitstream" \
  --codec_type AEIC-ME \
  --use_practical_entropy_coding \
  --y_quant_step 1.13 \
  --compile_model False \
  --enable_xformers_memory_efficient_attention False \
  --color_fix False \
  --merge_LoRA True \
  --use_tiled_vae True \
  --use_tiled_unet True \
  --vae_decoder_tiled_size 160 \
  --latent_tiled_size 96 \
  --latent_tiled_overlap 32

# The recovered compressor can skip an image after CUDA OOM. Check completeness.
"$PYTHON_BIN" - "$INPUT_DIR" "$OUTPUT_DIR" <<'PY'
from pathlib import Path
import sys
inputs = {p.stem for p in Path(sys.argv[1]).glob("*.png")}
if not inputs:
    raise SystemExit("No PNG inputs found")
output = Path(sys.argv[2])
for directory, suffix in [("bitstream", ".bin"), ("reconstructed", ".png")]:
    produced = {p.stem for p in (output / directory).glob("*" + suffix)}
    if produced != inputs:
        raise SystemExit(f"Incomplete or stale {directory}: missing={sorted(inputs-produced)}, extra={sorted(produced-inputs)}")
print(f"Recovered runtime completed: {len(inputs)} images. Audit outputs before comparing challenge results.")
PY
