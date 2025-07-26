#!/bin/bash

echo "================================================"
echo "AI Medical Assistant - Setup Script"
echo "================================================"
echo

echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

python3 --version

echo
echo "Installing Python dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo
echo "================================================"
echo "Setup completed successfully!"
echo "================================================"
echo
echo "NEXT STEPS:"
echo "1. Install Tesseract OCR:"
echo "   - macOS: brew install tesseract"
echo "   - Ubuntu/Debian: sudo apt-get install tesseract-ocr"
echo "2. Get your free Gemini API key from: https://makersuite.google.com/app/apikey"
echo "3. Edit the .env file and add your API key"
echo "4. Run: python3 app.py"
echo "5. Open your browser to: http://localhost:5000"
echo
echo "================================================"
echo "Important Notes:"
echo "- This is for educational purposes only"
echo "- Always consult healthcare professionals for medical advice"
echo "- Do not use for emergency medical situations"
echo "================================================"
echo
