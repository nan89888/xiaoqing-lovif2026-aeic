#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python}"
cmake -S "$ROOT_DIR/recovered-aeic/src/cpp" \
  -B "$ROOT_DIR/recovered-aeic/src/build" \
  -DCMAKE_BUILD_TYPE=Release \
  -DPYTHON_EXECUTABLE="$(command -v "$PYTHON_BIN")"
cmake --build "$ROOT_DIR/recovered-aeic/src/build" --parallel "${BUILD_JOBS:-2}"
