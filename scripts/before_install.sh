#!/bin/bash
set -e

echo "=== Before Install Phase ==="
echo "Stopping existing application..."

# Stop Flask application if running
if pgrep -f "python.*app.py" > /dev/null; then
    echo "Killing existing Flask process..."
    pkill -f "python.*app.py" || true
else
    echo "No running Flask process found"
fi

# Remove old application directory
if [ -d "/home/ec2-user/app" ]; then
    echo "Removing old application directory..."
    rm -rf /home/ec2-user/app
fi

# Create fresh application directory
echo "Creating new application directory..."
mkdir -p /home/ec2-user/app

echo "=== Before Install Phase Complete ==="