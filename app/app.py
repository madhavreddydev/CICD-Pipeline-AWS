from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

# Home route
@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html')

# API route to get server status
@app.route('/api/status')
def get_status():
    """Return application status"""
    return jsonify({
        'status': 'success',
        'message': 'Flask application is running',
        'timestamp': datetime.now().isoformat(),
        'environment': os.getenv('FLASK_ENV', 'production')
    })

# API route to get application info
@app.route('/api/info')
def get_info():
    """Return application information"""
    return jsonify({
        'app_name': 'CI/CD Pipeline Demo',
        'version': '1.0.0',
        'author': 'DevOps Engineer',
        'deployment_date': datetime.now().isoformat()
    })

# Error handler for 404
@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Page not found',
        'status_code': 404
    }), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'status_code': 500
    }), 500

# Main entry point
if __name__ == '__main__':
    # Run Flask development server
    # In production, use Gunicorn instead
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )