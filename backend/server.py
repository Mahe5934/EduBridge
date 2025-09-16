#!/usr/bin/env python3
# =====================================================================================
# File: EduBridge/backend/server.py
# Description: Main server implementation for EduBridge backend
# Created: 2025-09-16 10:24:25
# Last Modified: 2025-09-16 10:24:25
# =====================================================================================

import http.server
import socketserver
import json
import os
import urllib.parse
from http import HTTPStatus
import mimetypes
import logging
from pathlib import Path

# Import our modules
from api import APIHandler
from utils import get_content_type, load_json_data, save_json_data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backend/logs/server.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EduBridgeHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler for EduBridge"""
    
    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from
        super().__init__(*args, directory="frontend", **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        logger.info(f"GET request for {self.path}")
        
        # Parse the URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        
        # Handle API endpoints
        if path.startswith('/api/'):
            api_handler = APIHandler()
            response = api_handler.handle_get(path, {})
            self._send_api_response(response)
            return
        
        # Handle static files
        if path == '/' or path == '/index.html':
            self.path = '/index.html'
        elif path == '/courses':
            self.path = '/courses.html'
        elif path == '/about':
            self.path = '/about.html'
        
        # Serve static files using parent class method
        return super().do_GET()
    
    def do_POST(self):
        """Handle POST requests"""
        logger.info(f"POST request for {self.path}")
        
        # Parse the URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        
        # Get content length
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read the POST data
        post_data = self.rfile.read(content_length)
        
        # Parse JSON data if content type is JSON
        data = {}
        if self.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                self._send_error_response(HTTPStatus.BAD_REQUEST, "Invalid JSON data")
                return
        
        # Handle API endpoints
        if path.startswith('/api/'):
            api_handler = APIHandler()
            response = api_handler.handle_post(path, data)
            self._send_api_response(response)
            return
        
        # If we get here, it's an unknown endpoint
        self._send_error_response(HTTPStatus.NOT_FOUND, "Endpoint not found")
    
    def do_PUT(self):
        """Handle PUT requests"""
        logger.info(f"PUT request for {self.path}")
        
        # Parse the URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        
        # Get content length
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read the PUT data
        put_data = self.rfile.read(content_length)
        
        # Parse JSON data if content type is JSON
        data = {}
        if self.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(put_data.decode('utf-8'))
            except json.JSONDecodeError:
                self._send_error_response(HTTPStatus.BAD_REQUEST, "Invalid JSON data")
                return
        
        # Handle API endpoints
        if path.startswith('/api/'):
            api_handler = APIHandler()
            response = api_handler.handle_put(path, data)
            self._send_api_response(response)
            return
        
        # If we get here, it's an unknown endpoint
        self._send_error_response(HTTPStatus.NOT_FOUND, "Endpoint not found")
    
    def do_DELETE(self):
        """Handle DELETE requests"""
        logger.info(f"DELETE request for {self.path}")
        
        # Parse the URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        
        # Handle API endpoints
        if path.startswith('/api/'):
            api_handler = APIHandler()
            response = api_handler.handle_delete(path)
            self._send_api_response(response)
            return
        
        # If we get here, it's an unknown endpoint
        self._send_error_response(HTTPStatus.NOT_FOUND, "Endpoint not found")
    
    def _send_api_response(self, response):
        """Send API response to client"""
        # Set CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        
        # Send response
        self.send_response(response['status'])
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        # Send response data
        if 'data' in response:
            self.wfile.write(json.dumps(response['data']).encode('utf-8'))
    
    def _send_error_response(self, status_code, message):
        """Send error response to client"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        error_response = {
            'error': message,
            'status': status_code
        }
        self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS"""
        self.send_response(HTTPStatus.OK)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

class EduBridgeServer:
    """Main server class for EduBridge"""
    
    def __init__(self, port=8000):
        self.port = port
        self.server = None
        
        # Create necessary directories
        os.makedirs('backend/data', exist_ok=True)
        os.makedirs('backend/logs', exist_ok=True)
        
        # Initialize data files if they don't exist
        self._initialize_data_files()
    
    def _initialize_data_files(self):
        """Initialize data files with empty structures if they don't exist"""
        data_files = {
            'backend/data/courses.json': [],
            'backend/data/lectures.json': [],
            'backend/data/notes.json': [],
            'backend/data/quizzes.json': []
        }
        
        for file_path, default_content in data_files.items():
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    json.dump(default_content, f, indent=2)
                logger.info(f"Created {file_path} with default content")
    
    def start(self):
        """Start the server"""
        try:
            # Create socket server
            with socketserver.TCPServer(("", self.port), EduBridgeHTTPRequestHandler) as self.server:
                logger.info(f"EduBridge server started on port {self.port}")
                logger.info(f"Visit http://localhost:{self.port} to access the application")
                
                # Start serving requests
                self.server.serve_forever()
        except KeyboardInterrupt:
            logger.info("Server stopped by user")
        except Exception as e:
            logger.error(f"Server error: {e}")
        finally:
            if self.server:
                self.server.server_close()
                logger.info("Server closed")

if __name__ == "__main__":
    # Create and start the server
    server = EduBridgeServer()
    server.start()