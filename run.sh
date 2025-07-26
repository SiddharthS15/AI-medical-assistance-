#!/bin/bash

echo "================================================"
echo "   AI Medical Assistant - Quick Start"
echo "================================================"
echo

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Error: .env file not found!"
    echo "Please copy .env.example to .env and add your API keys"
    exit 1
fi

echo "Starting AI Medical Assistant..."
echo "Open your browser to: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo

python3 app.py
