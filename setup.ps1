# Setup venv untuk project Surat Maaf (Windows PowerShell).
# Kalau py launcher tidak punya versi 3.14, ganti angka versi di bawah
# sesuai Python yang terinstal (cek dengan: py -0).

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

$pyVersion = "-3.14"

if (Get-Command py -ErrorAction SilentlyContinue) {
    $available = (py -0p) 2>$null
    if ($available -notmatch [regex]::Escape($pyVersion)) {
        Write-Host "Python $pyVersion tidak ditemukan lewat 'py launcher', pakai versi default." -ForegroundColor Yellow
        $pyVersion = ""
    }
    py $pyVersion -m venv .venv
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    python -m venv .venv
} else {
    Write-Host "Python tidak ditemukan. Install dulu dari python.org." -ForegroundColor Red
    exit 1
}

.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host ""
Write-Host "Selesai. Selanjutnya jalankan:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "  streamlit run app.py"
