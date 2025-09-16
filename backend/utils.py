# =====================================================================================
# File: EduBridge/backend/utils.py
# Description: Utility functions for EduBridge backend
# Created: 2025-09-16 10:27:09
# Last Modified: 2025-09-16 10:27:09
# =====================================================================================

import json
import os
import mimetypes
import hashlib
import secrets
import logging
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

# Configure logger
logger = logging.getLogger(__name__)

def get_content_type(file_path: str) -> str:
    """Get MIME content type for a file path"""
    content_type, _ = mimetypes.guess_type(file_path)
    return content_type or 'application/octet-stream'

def load_json_data(file_path: str) -> Union[List[Any], Dict[str, Any]]:
    """Load JSON data from file, return empty list/dict if file doesn't exist"""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Return appropriate empty structure based on file name
            if file_path.endswith(('courses.json', 'lectures.json', 'notes.json', 'quizzes.json')):
                return []
            else:
                return {}
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Error loading JSON data from {file_path}: {e}")
        # Return appropriate empty structure based on file name
        if file_path.endswith(('courses.json', 'lectures.json', 'notes.json', 'quizzes.json')):
            return []
        else:
            return {}

def save_json_data(file_path: str, data: Union[List[Any], Dict[str, Any]]) -> bool:
    """Save JSON data to file"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except (TypeError, IOError) as e:
        logger.error(f"Error saving JSON data to {file_path}: {e}")
        return False

def generate_id() -> str:
    """Generate a unique ID"""
    return secrets.token_hex(16)

def hash_password(password: str) -> str:
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against its hash"""
    return hash_password(password) == hashed

def sanitize_input(input_str: str) -> str:
    """Sanitize user input to prevent XSS attacks"""
    # Remove or escape potentially dangerous characters
    sanitized = input_str.replace('<', '<').replace('>', '>')
    sanitized = sanitized.replace('"', '"').replace("'", '&#x27;')
    return sanitized

def validate_email(email: str) -> bool:
    """Validate email format"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> Dict[str, str]:
    """Validate required fields in data and return errors"""
    errors = {}
    for field in required_fields:
        if field not in data or not data[field]:
            errors[field] = f"{field} is required"
    return errors

def format_datetime(dt_string: str) -> str:
    """Format datetime string for display"""
    try:
        dt = datetime.fromisoformat(dt_string.replace('Z', '+00:00'))
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except ValueError:
        return dt_string

def calculate_duration_minutes(hours: int = 0, minutes: int = 0) -> int:
    """Calculate total duration in minutes"""
    return hours * 60 + minutes

def format_duration(duration_minutes: int) -> str:
    """Format duration in minutes to human-readable string"""
    if duration_minutes < 60:
        return f"{duration_minutes} min"
    else:
        hours = duration_minutes // 60
        minutes = duration_minutes % 60
        if minutes > 0:
            return f"{hours} hr {minutes} min"
        else:
            return f"{hours} hr"

def search_in_text(text: str, search_terms: List[str]) -> bool:
    """Check if all search terms are found in text (case insensitive)"""
    if not search_terms:
        return True
    
    text_lower = text.lower()
    return all(term.lower() in text_lower for term in search_terms)

def filter_by_category(items: List[Dict[str, Any]], category: str) -> List[Dict[str, Any]]:
    """Filter items by category"""
    if category == 'all' or not category:
        return items
    return [item for item in items if item.get('category', '').lower() == category.lower()]

def sort_items(items: List[Dict[str, Any]], sort_by: str) -> List[Dict[str, Any]]:
    """Sort items based on sort_by parameter"""
    if sort_by == 'a-z':
        return sorted(items, key=lambda x: x.get('title', '').lower())
    elif sort_by == 'z-a':
        return sorted(items, key=lambda x: x.get('title', '').lower(), reverse=True)
    elif sort_by == 'duration':
        return sorted(items, key=lambda x: x.get('duration', 0))
    elif sort_by == 'newest':
        return sorted(items, key=lambda x: x.get('created_at', ''), reverse=True)
    else:  # Default to popular (original order)
        return items

def paginate_items(items: List[Any], page: int = 1, per_page: int = 10) -> Dict[str, Any]:
    """Paginate items"""
    total_items = len(items)
    total_pages = (total_items + per_page - 1) // per_page
    
    # Ensure page is within valid range
    page = max(1, min(page, total_pages))
    
    # Calculate start and end indices
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    
    # Get paginated items
    paginated_items = items[start_idx:end_idx]
    
    return {
        'items': paginated_items,
        'page': page,
        'per_page': per_page,
        'total_items': total_items,
        'total_pages': total_pages
    }

def create_search_index_item(content_type: str, content_id: str, title: str, 
                           description: str, category: str, tags: List[str]) -> Dict[str, Any]:
    """Create a search index item"""
    return {
        'id': generate_id(),
        'content_type': content_type,
        'content_id': content_id,
        'title': title,
        'description': description,
        'category': category,
        'tags': tags,
        'created_at': datetime.now().isoformat()
    }

def update_timestamps(data: Dict[str, Any]) -> Dict[str, Any]:
    """Update timestamps in data dict"""
    now = datetime.now().isoformat()
    if 'created_at' not in data:
        data['created_at'] = now
    data['updated_at'] = now
    return data

def get_file_size(file_path: str) -> int:
    """Get file size in bytes"""
    try:
        return os.path.getsize(file_path)
    except OSError:
        return 0

def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format"""
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f} {size_names[i]}"

def is_valid_id(id_str: str) -> bool:
    """Validate if string is a valid hex ID"""
    try:
        int(id_str, 16)
        return len(id_str) == 32  # 16 bytes = 32 hex characters
    except ValueError:
        return False

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent directory traversal"""
    # Remove path separators and parent directory references
    sanitized = filename.replace('/', '_').replace('\\', '_').replace('..', '')
    # Remove any other potentially dangerous characters
    sanitized = ''.join(c for c in sanitized if c.isalnum() or c in '._- ')
    return sanitized.strip() or 'unnamed_file'

def get_content_preview(content: str, max_length: int = 100) -> str:
    """Get preview of content text"""
    if len(content) <= max_length:
        return content
    return content[:max_length].rstrip() + '...'

# Error handling utilities
class APIError(Exception):
    """Custom API error exception"""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def handle_api_error(error: Exception) -> Dict[str, Any]:
    """Handle API errors and return standardized error response"""
    if isinstance(error, APIError):
        return {
            'status': error.status_code,
            'error': error.message
        }
    else:
        logger.error(f"Unexpected error: {error}", exc_info=True)
        return {
            'status': 500,
            'error': 'Internal server error'
        }