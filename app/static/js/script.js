// DOM Elements
const statusIndicator = document.getElementById('statusIndicator');
const statusText = document.getElementById('statusText');
const statusMessage = document.getElementById('statusMessage');
const appInfo = document.getElementById('appInfo');

// Check application status
function checkStatus() {
    console.log('Checking application status...');
    
    // Change button to loading state
    const btn = event.target;
    btn.disabled = true;
    btn.textContent = 'Checking...';
    
    // Fetch status from API
    fetch('/api/status')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Status received:', data);
            
            // Update status indicator
            statusIndicator.classList.add('active');
            statusText.textContent = 'Online';
            statusText.style.color = '#51cf66';
            
            // Update message
            statusMessage.textContent = `✓ ${data.message} | Timestamp: ${new Date(data.timestamp).toLocaleString()}`;
            statusMessage.style.color = '#51cf66';
            
            // Reset button
            btn.disabled = false;
            btn.textContent = 'Refresh Status';
        })
        .catch(error => {
            console.error('Error checking status:', error);
            
            // Update status to offline
            statusIndicator.classList.remove('active');
            statusText.textContent = 'Offline';
            statusText.style.color = '#ff6b6b';
            
            // Update message
            statusMessage.textContent = `✗ Failed to connect to server: ${error.message}`;
            statusMessage.style.color = '#ff6b6b';
            
            // Reset button
            btn.disabled = false;
            btn.textContent = 'Refresh Status';
        });
}

// Get application information
function getAppInfo() {
    console.log('Fetching application info...');
    
    // Change button to loading state
    const btn = event.target;
    btn.disabled = true;
    btn.textContent = 'Loading...';
    
    // Update display to show loading
    appInfo.innerHTML = '<p style="color: #667eea;">Loading application information...</p>';
    
    // Fetch app info from API
    fetch('/api/info')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('App info received:', data);
            
            // Format and display info
            const infoHTML = `
                <div style="line-height: 1.8;">
                    <strong>App Name:</strong> ${data.app_name}<br>
                    <strong>Version:</strong> ${data.version}<br>
                    <strong>Author:</strong> ${data.author}<br>
                    <strong>Deployment Date:</strong> ${new Date(data.deployment_date).toLocaleString()}<br>
                </div>
            `;
            
            appInfo.innerHTML = infoHTML;
            
            // Reset button
            btn.disabled = false;
            btn.textContent = 'Load App Info';
        })
        .catch(error => {
            console.error('Error fetching app info:', error);
            
            // Show error message
            appInfo.innerHTML = `<p style="color: #ff6b6b;">Error loading app info: ${error.message}</p>`;
            
            // Reset button
            btn.disabled = false;
            btn.textContent = 'Load App Info';
        });
}

// Auto-check status when page loads
document.addEventListener('DOMContentLoaded', function() {
    console.log('Page loaded, checking initial status...');
    
    // Simulate button click to check status
    setTimeout(() => {
        fetch('/api/status')
            .then(response => response.json())
            .then(data => {
                statusIndicator.classList.add('active');
                statusText.textContent = 'Online';
                statusText.style.color = '#51cf66';
                statusMessage.textContent = `✓ ${data.message}`;
                statusMessage.style.color = '#51cf66';
            })
            .catch(error => {
                console.error('Initial status check failed:', error);
                statusIndicator.classList.remove('active');
                statusText.textContent = 'Offline';
                statusText.style.color = '#ff6b6b';
                statusMessage.textContent = 'Failed to connect to server';
                statusMessage.style.color = '#ff6b6b';
            });
    }, 500);
});

// Log when script loads
console.log('script.js loaded successfully');