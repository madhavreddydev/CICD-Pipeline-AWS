import pytest
import json
from app.app import app

# Test fixtures
@pytest.fixture
def client():
    """Create test client for Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test home page route
def test_home_page(client):
    """Test that home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'CI/CD Pipeline Demo' in response.data

# Test home page contains expected content
def test_home_page_content(client):
    """Test that home page has required content"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Application Status' in response.data
    assert b'Pipeline Information' in response.data
    assert b'AWS CodeBuild' in response.data
    assert b'AWS CodeDeploy' in response.data

# Test API status endpoint
def test_api_status(client):
    """Test /api/status endpoint"""
    response = client.get('/api/status')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'message' in data
    assert 'timestamp' in data
    assert 'environment' in data

# Test API status response format
def test_api_status_json_format(client):
    """Test that status endpoint returns valid JSON"""
    response = client.get('/api/status')
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert isinstance(data, dict)
    assert 'status' in data
    assert 'message' in data

# Test API info endpoint
def test_api_info(client):
    """Test /api/info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'app_name' in data
    assert 'version' in data
    assert 'author' in data
    assert 'deployment_date' in data

# Test API info response values
def test_api_info_values(client):
    """Test that info endpoint contains expected values"""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['app_name'] == 'CI/CD Pipeline Demo'
    assert data['version'] == '1.0.0'
    assert data['author'] == 'DevOps Engineer'

# Test 404 error handling
def test_404_error(client):
    """Test that 404 errors are handled correctly"""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
    
    data = json.loads(response.data)
    assert data['error'] == 'Page not found'
    assert data['status_code'] == 404

# Test API endpoints are accessible
def test_all_endpoints_accessible(client):
    """Test that all main endpoints are accessible"""
    endpoints = [
        ('/', 200),
        ('/api/status', 200),
        ('/api/info', 200),
    ]
    
    for endpoint, expected_status in endpoints:
        response = client.get(endpoint)
        assert response.status_code == expected_status, f"Endpoint {endpoint} returned {response.status_code}"

# Test response headers
def test_response_headers(client):
    """Test that responses have correct headers"""
    response = client.get('/api/status')
    assert 'Content-Type' in response.headers
    assert response.headers['Content-Type'] == 'application/json'

# Test that app initializes without errors
def test_app_initialization():
    """Test that Flask app initializes correctly"""
    assert app is not None
    assert app.config['SECRET_KEY'] == 'your-secret-key-change-this'

# Test app is in testing mode
def test_app_test_mode():
    """Test that app can be set to testing mode"""
    app.config['TESTING'] = True
    assert app.config['TESTING'] is True

if __name__ == '__main__':
    pytest.main([__file__, '-v'])