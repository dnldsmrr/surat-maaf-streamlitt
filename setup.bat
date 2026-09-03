@echo off
REM Setup venv untuk project Surat Maaf (Windows).
cd /d %~dp0

where python >nul 2>nul
if errorlevel 1 (
  echo Python tidak ditemukan. Install Python dulu dari python.org.
  exit /b 1
)

python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Selesai. Selanjutnya jalankan:
echo   venv\Scripts\activate
echo   streamlit run app.py
