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

echo "=== Before Install Phase Complete ==="