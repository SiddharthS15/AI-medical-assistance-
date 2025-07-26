@echo off
echo ================================================
echo   AI Medical Assistant - Starting Application
echo ================================================
echo.

echo Checking for .env file...
if not exist ".env" (
    echo ERROR: .env file not found!
    echo Please run setup.bat first or copy .env.example to .env
    echo and add your Gemini API key.
    echo.
    pause
    exit /b 1
)

echo Starting Flask application...
echo.
echo ============================================
echo Your AI Medical Assistant is starting...
echo ============================================
echo.
echo Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
