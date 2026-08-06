#!/bin/bash
set -e

echo "=== Application Start Phase ==="
echo "Starting Flask application..."

# Navigate to application directory
cd /home/ec2-user/app

# Get the current date and time
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "Application start time: $TIMESTAMP"

# Start Flask app in background
echo "Launching Flask server on port 5000..."
nohup python app.py > /tmp/flask_app.log 2>&1 &

# Wait for app to start
sleep 2

# Check if Flask is running
if pgrep -f "python.*app.py" > /dev/null; then
    echo "Flask application started successfully"
    echo "Application is running on http://localhost:5000"
else
    echo "Failed to start Flask application"
    exit 1
fi

echo "=== Application Start Phase Complete ==="