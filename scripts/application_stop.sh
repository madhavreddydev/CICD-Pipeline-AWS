#!/bin/bash
set -e

echo "=== Application Stop Phase ==="
echo "Stopping Flask application..."

# Check if Flask process is running
if pgrep -f "python.*app.py" > /dev/null; then
    echo "Found running Flask process..."
    
    # Gracefully kill Flask
    echo "Stopping Flask gracefully..."
    pkill -f "python.*app.py" || true
    
    # Wait for process to stop
    sleep 2
    
    # Verify it stopped
    if pgrep -f "python.*app.py" > /dev/null; then
        echo "Process still running, force killing..."
        pkill -9 -f "python.*app.py" || true
    fi
    
    echo "Flask application stopped successfully"
else
    echo "No running Flask process found"
fi

# Clean up log files (optional)
if [ -f "/tmp/flask_app.log" ]; then
    echo "Cleaning up log files..."
    rm -f /tmp/flask_app.log
fi

echo "=== Application Stop Phase Complete ==="