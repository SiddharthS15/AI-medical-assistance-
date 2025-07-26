@echo off
echo ================================================
echo AI Medical Assistant - Setup Script
echo ================================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo.
echo Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Checking for .env file...
if not exist ".env" (
    echo Creating .env file from template...
    copy ".env.example" ".env"
    echo.
    echo IMPORTANT: Please edit .env file and add your API keys:
    echo 1. Get Gemini API key from: https://makersuite.google.com/app/apikey
    echo 2. Add your API key to .env file
    echo 3. Update Tesseract path if needed
    echo.
) else (
    echo .env file already exists
)

echo.
echo ================================================
echo Setup completed successfully!
echo ================================================
echo.
echo NEXT STEPS:
echo 1. Make sure Tesseract OCR is installed
echo 2. Edit .env file with your Gemini API key
echo 3. Run: python app.py
echo 4. Open browser to: http://localhost:5000
echo.
echo For help, see README.md and API_SETUP_GUIDE.md
echo.
pause
