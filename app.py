"""
Simple HTTP server for Meta App Repository - Python Flask Implementation

This is a Python 3 Flask application that replicates the exact functionality of the Node.js
server.js implementation. It responds to all HTTP requests with "Hello, World!" message.
This server binds only to localhost (127.0.0.1) on port 3000 for security.

The server handles ALL HTTP methods (GET, POST, PUT, DELETE, etc.) and ALL paths with the same
static response, maintaining feature parity with the Node.js version.

Requirements:
    - Python 3.7+
    - Flask 3.0+

Usage:
    python3 app.py

Access:
    Navigate to http://127.0.0.1:3000 in your browser
    Or use curl: curl http://127.0.0.1:3000

Version: 1.0.0
"""

from flask import Flask, Response

# Server hostname configuration
# The server binds only to localhost (127.0.0.1), preventing external network access for security.
# This means the server is only accessible from the same machine it's running on.
# For production deployment allowing external access, change to '0.0.0.0' to bind to all network
# interfaces, or specify a particular IP address.
HOSTNAME = '127.0.0.1'

# Server port number configuration
# Port 3000 is commonly used for development servers. If this port is already in use
# by another application, modify this value to an available port (e.g., 3001, 8080, 8000).
# Consider using environment variables for flexible configuration across different deployment environments.
PORT = 3000

# Create Flask application instance
app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def handle_all_requests(path):
    """
    HTTP request handler that processes all incoming requests.
    
    This function handles ALL HTTP methods (GET, POST, PUT, DELETE, PATCH, etc.) and
    ALL URL paths with the same static response. No request parsing, routing, or method filtering
    is implemented. Every request receives a 200 OK status with "Hello, World!" in plain text.
    
    This exactly replicates the behavior of the Node.js server.js implementation.
    
    Args:
        path (str): The URL path (ignored, all paths return same response)
    
    Returns:
        Response: Flask Response object with status 200, Content-Type text/plain, 
                  and body "Hello, World!\\n"
    """
    return Response('Hello, World!\n', status=200, mimetype='text/plain')

if __name__ == '__main__':
    """
    Start the Flask development server and bind it to the specified hostname and port.
    The server logs startup information to the console for confirmation.
    
    Note: Flask's development server automatically logs the server URL when it starts.
    """
    print(f'Server running at http://{HOSTNAME}:{PORT}/')
    # Run Flask development server
    # debug=False for production-like behavior
    # use_reloader=False to prevent double startup in development
    app.run(host=HOSTNAME, port=PORT, debug=False)
