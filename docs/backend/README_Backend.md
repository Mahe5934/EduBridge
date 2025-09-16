# EduBridge Backend Documentation

## Overview

The EduBridge backend is a lightweight Python server built using the built-in `http.server` module. It provides a RESTful API for managing educational content including courses, lectures, notes, and quizzes. The backend is designed to be simple, lightweight, and easy to deploy in resource-constrained environments typical of rural colleges.

## Key Features

### API Endpoints
- Full CRUD operations for courses, lectures, notes, and quizzes
- RESTful design with proper HTTP status codes
- JSON request/response format
- CORS support for cross-origin requests

### Data Management
- JSON file-based storage for all educational content
- Automatic data file initialization
- Data validation and sanitization
- Unique ID generation for all entities

### Security
- Input sanitization to prevent injection attacks
- File path validation to prevent directory traversal
- CORS headers for controlled cross-origin access

### Performance
- Lightweight implementation with minimal dependencies
- Efficient JSON data handling
- Proper error handling and logging

## Project Structure

```
backend/
├── api.py              # REST API endpoints implementation
├── models.py           # Data models and structures
├── server.py           # Main server implementation
├── utils.py            # Utility functions and helpers
├── data/               # JSON data storage
│   ├── courses.json
│   ├── lectures.json
│   ├── notes.json
│   └── quizzes.json
└── logs/
    └── server.log      # Server activity logs
```

## API Endpoints

### Courses

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/courses` | GET | Retrieve all courses |
| `/api/courses/{id}` | GET | Retrieve a specific course |
| `/api/courses` | POST | Create a new course |
| `/api/courses/{id}` | PUT | Update an existing course |
| `/api/courses/{id}` | DELETE | Delete a course |

#### Course Object Structure
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "category": "string",
  "duration": "integer",
  "lectures_count": "integer",
  "instructor": "string",
  "thumbnail": "string",
  "level": "string"
}
```

### Lectures

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/lectures` | GET | Retrieve all lectures |
| `/api/lectures/{id}` | GET | Retrieve a specific lecture |
| `/api/lectures` | POST | Create a new lecture |
| `/api/lectures/{id}` | PUT | Update an existing lecture |
| `/api/lectures/{id}` | DELETE | Delete a lecture |

#### Lecture Object Structure
```json
{
  "id": "string",
  "course_id": "string",
  "title": "string",
  "description": "string",
  "duration": "integer",
  "video_url": "string",
  "order": "integer"
}
```

### Notes

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/notes` | GET | Retrieve all notes |
| `/api/notes/{id}` | GET | Retrieve a specific note |
| `/api/notes` | POST | Create a new note |
| `/api/notes/{id}` | PUT | Update an existing note |
| `/api/notes/{id}` | DELETE | Delete a note |

#### Note Object Structure
```json
{
  "id": "string",
  "course_id": "string",
  "lecture_id": "string",
  "title": "string",
  "content": "string",
  "file_url": "string"
}
```

### Quizzes

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/quizzes` | GET | Retrieve all quizzes |
| `/api/quizzes/{id}` | GET | Retrieve a specific quiz |
| `/api/quizzes` | POST | Create a new quiz |
| `/api/quizzes/{id}` | PUT | Update an existing quiz |
| `/api/quizzes/{id}` | DELETE | Delete a quiz |

#### Quiz Object Structure
```json
{
  "id": "string",
  "course_id": "string",
  "lecture_id": "string",
  "title": "string",
  "questions": "array"
}
```

## Data Models

### Course
Represents an educational course with metadata and content references.

### Lecture
Represents a lecture within a course, including video content and metadata.

### Note
Represents notes associated with a specific lecture or course.

### Quiz
Represents a quiz with questions for assessing student knowledge.

### Question
Represents a question within a quiz with multiple choice options.

### User
Represents a user account for authentication (planned for future implementation).

## Implementation Details

### Server Implementation
The server is implemented using Python's built-in `http.server` module with custom request handlers for API endpoints and static file serving.

### API Handler
The API handler routes requests to appropriate functions based on the URL path and HTTP method, implementing full CRUD operations for all content types.

### Data Models
Data models are implemented using Python dataclasses for type safety and consistency. Each model includes validation and serialization methods.

### Utilities
Utility functions provide common functionality such as JSON data loading/saving, ID generation, input sanitization, and error handling.

## Security Considerations

### Input Validation
All user inputs are sanitized to prevent injection attacks and ensure data integrity.

### File Access
File paths are validated to prevent directory traversal attacks and unauthorized file access.

### CORS
Cross-Origin Resource Sharing is properly configured to allow legitimate cross-origin requests while blocking malicious ones.

## Performance Optimization

### Lightweight Design
The backend uses minimal dependencies and efficient data handling to ensure fast response times.

### JSON Storage
Data is stored in JSON files for simplicity and ease of deployment without requiring a database server.

### Caching Considerations
While the current implementation doesn't include caching, the architecture supports future caching implementations.

## Error Handling

### HTTP Status Codes
Proper HTTP status codes are returned for all API responses:
- 200: Success
- 201: Created
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

### Error Responses
All error responses follow a consistent format:
```json
{
  "error": "Error message",
  "status": 400
}
```

## Logging

### Log Files
Server activity is logged to `backend/logs/server.log` with timestamps and log levels.

### Log Format
Logs include timestamp, logger name, log level, and message for easy debugging and monitoring.

## Deployment

### Requirements
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

### Running the Server
```bash
python backend/server.py
```

### Configuration
The server runs on port 8000 by default but can be configured in `server.py`.

## Extending the Backend

### Adding New Content Types
To add new content types:
1. Create a new model in `models.py`
2. Add data storage in `server.py`
3. Implement API endpoints in `api.py`

### Customizing Data Storage
The backend can be extended to use different storage mechanisms by modifying the utility functions in `utils.py`.

## Best Practices

### Code Organization
- Keep handlers focused on request routing
- Implement business logic in separate functions
- Use utility functions for common operations
- Maintain consistent error handling

### Data Integrity
- Validate all inputs
- Sanitize user data
- Use transactions when modifying multiple data files
- Implement proper error recovery

### Security
- Never trust client-side data
- Validate all inputs
- Sanitize outputs
- Implement proper authentication for production use

## Future Enhancements

### Authentication
Implement user authentication and authorization for secure access to educational content.

### Database Integration
Replace JSON file storage with a proper database for better performance and scalability.

### Caching
Implement caching mechanisms to improve response times for frequently accessed content.

### Search Functionality
Enhance search capabilities with full-text search and filtering options.

### Analytics
Add usage tracking and analytics to monitor platform engagement and content effectiveness.