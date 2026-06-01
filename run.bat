@echo off

cd /d "%~dp0"

if not exist venv (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo [INFO] Installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt

if not exist output (
    mkdir output
)

echo [INFO] Starting OmniConvert...
python main.py

pause