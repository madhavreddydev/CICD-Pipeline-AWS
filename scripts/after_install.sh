#!/bin/bash
set -e

echo "=== After Install Phase ==="
echo "Installing Python dependencies..."

# Navigate to application directory
cd /home/ec2-user/app

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing Flask and dependencies..."
pip install -r requirements.txt

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully"
else
    echo "Failed to install dependencies"
    exit 1
fi

echo "=== After Install Phase Complete ==="