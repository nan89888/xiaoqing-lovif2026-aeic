#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT_DIR/upstream-aeic"
REPO="https://github.com/LuizScarlet/AEIC.git"
COMMIT="7222c2c85e8db7ea0b829a139313ab7f4fdea88c"

if [[ -e "$DEST" ]]; then
  echo "Refusing to overwrite existing $DEST" >&2
  exit 1
fi

git clone "$REPO" "$DEST"
git -C "$DEST" checkout --detach "$COMMIT"
echo "Pinned AEIC source at $(git -C "$DEST" rev-parse HEAD)"
