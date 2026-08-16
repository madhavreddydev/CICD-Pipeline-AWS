#!/bin/bash
set -e

cd /home/ec2-user/app/app

pkill -f "python3.*app.py" || true

nohup /home/ec2-user/app/venv/bin/python app.py > /tmp/flask_app.log 2>&1 &

sleep 3

if pgrep -f "venv/bin/python.*app.py" >/dev/null; then
    echo "Flask application started successfully"
else
    echo "Flask application failed"
    cat /tmp/flask_app.log
    exit 1
fi