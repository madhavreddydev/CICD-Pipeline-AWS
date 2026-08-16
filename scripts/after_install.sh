#!/bin/bash
set -e

echo "=== After Install Phase ==="

cd /home/ec2-user/app

echo "Python:"
python3 --version

echo "Installing pip if needed..."
if ! python3 -m pip --version >/dev/null 2>&1; then
    dnf install -y python3-pip
fi

echo "Creating virtual environment..."
rm -rf /home/ec2-user/app/venv
python3 -m venv /home/ec2-user/app/venv

echo "Installing dependencies..."
/home/ec2-user/app/venv/bin/python -m pip install -r /home/ec2-user/app/requirements.txt

echo "=== After Install Complete ==="