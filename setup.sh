#!/bin/bash
set -e

GOOGLE_DRIVE_ID="0B7XkCwpI5KDYNlNUTTlSS21pQmM"
FILE_NAME="GoogleNews-vectors.bin.gz"
TARGET_DIR="src/copus"

uv venv
source .venv/bin/activate
uv pip install gdown

mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

gdown "https://drive.google.com/uc?id=${GOOGLE_DRIVE_ID}" -O "$FILE_NAME"

if [ -f "$FILE_NAME" ]; then
    gunzip -f "$FILE_NAME"
    echo "✅ Download and extraction completed"
else
    echo "❌ Failed to download file"
    exit 1
fi

cd ../../

uv tool install git+https://github.com/j341nono/word2vequiz.git
