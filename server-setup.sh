#!/bin/bash
# Ubuntu/Debian setup script

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install -y python3 python3-pip python3-venv

# Install Tesseract OCR
sudo apt install -y tesseract-ocr tesseract-ocr-eng

# Install Nginx (optional - for reverse proxy)
sudo apt install -y nginx

# Install system dependencies for Python packages
sudo apt install -y python3-dev build-essential libffi-dev

# Create application directory
sudo mkdir -p /var/www/medical-assistant
cd /var/www/medical-assistant

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Create systemd service file
sudo tee /etc/systemd/system/medical-assistant.service > /dev/null <<EOF
[Unit]
Description=AI Medical Assistant
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/medical-assistant
Environment="PATH=/var/www/medical-assistant/venv/bin"
ExecStart=/var/www/medical-assistant/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl enable medical-assistant
sudo systemctl start medical-assistant
