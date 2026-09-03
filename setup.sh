#!/usr/bin/env bash
# Setup venv untuk project Surat Maaf (Linux/macOS).
set -e
cd "$(dirname "$0")"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 tidak ditemukan. Install Python 3 dulu." >&2
  exit 1
fi

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Selesai. Selanjutnya jalankan:"
echo "  source venv/bin/activate"
echo "  streamlit run app.py"
