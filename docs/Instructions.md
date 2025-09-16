# EduBridge - Running Instructions

## System Requirements

Before running EduBridge, ensure you have the following installed:
- Python 3.6 or higher
- A modern web browser (Chrome, Firefox, Safari, Edge)

## Quick Start

1. Clone or download the EduBridge repository
2. Navigate to the project root directory
3. Start the backend server:
   ```bash
   python backend/server.py
   ```
4. Open your browser and visit `http://localhost:8000`

## Detailed Setup Instructions

### Backend Setup

The backend is a lightweight Python server that serves both the frontend files and provides a REST API for educational content.

1. **Start the Server**
   ```bash
   python backend/server.py
   ```

2. **Server Features**
   - Serves static frontend files (HTML, CSS, JavaScript)
   - Provides RESTful API endpoints for courses, lectures, notes, and quizzes
   - Handles all HTTP methods (GET, POST, PUT, DELETE)
   - Implements CORS for cross-origin requests
   - Logs all requests to `backend/logs/server.log`

3. **API Endpoints**
   The backend provides the following REST API endpoints:
   - `GET /api/courses` - Retrieve all courses
   - `GET /api/courses/{id}` - Retrieve a specific course
   - `POST /api/courses` - Create a new course
   - `PUT /api/courses/{id}` - Update an existing course
   - `DELETE /api/courses/{id}` - Delete a course
   - Similar endpoints exist for lectures, notes, and quizzes

4. **Data Storage**
   All data is stored in JSON files located in `backend/data/`:
   - `courses.json` - Course information
   - `lectures.json` - Lecture content
   - `notes.json` - Course notes
   - `quizzes.json` - Quiz questions and answers

### Frontend Access

Once the backend server is running:

1. Open your web browser
2. Navigate to `http://localhost:8000`
3. You should see the EduBridge homepage

The frontend includes the following pages:
- **Homepage** (`/`) - Project overview and introduction
- **Courses** (`/courses.html`) - Browse available courses
- **Course Detail** (`/course-detail.html`) - Detailed course information
- **Lecture** (`/lecture.html`) - View lecture content
- **Notes** (`/notes.html`) - Access course notes
- **Quiz** (`/quiz.html`) - Take interactive quizzes
- **About** (`/about.html`) - Project information
- **Search** (`/search.html`) - Search across all content

## Development Workflow

### Modifying Content

Educational content can be modified by:
1. Directly editing the JSON files in `backend/data/`
2. Using the REST API endpoints to create, read, update, or delete content
3. Through future admin interface (planned enhancement)

### Customizing the Frontend

The frontend is built with pure HTML, CSS, and JavaScript:
- HTML files are located in the `frontend/` directory
- CSS is in `frontend/css/style.css`
- JavaScript functionality is in `frontend/js/main.js`

To customize the frontend:
1. Modify the HTML files to change content structure
2. Update CSS in `style.css` to change styling
3. Add functionality by editing `main.js`

### Testing API Endpoints

You can test the API endpoints using curl or any HTTP client:

1. **Retrieve all courses**
   ```bash
   curl http://localhost:8000/api/courses
   ```

2. **Create a new course**
   ```bash
   curl -X POST http://localhost:8000/api/courses \
        -H "Content-Type: application/json" \
        -d '{"title": "New Course", "description": "Course description", "category": "technology"}'
   ```

3. **Update a course**
   ```bash
   curl -X PUT http://localhost:8000/api/courses/{course_id} \
        -H "Content-Type: application/json" \
        -d '{"title": "Updated Course Title"}'
   ```

4. **Delete a course**
   ```bash
   curl -X DELETE http://localhost:8000/api/courses/{course_id}
   ```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   If you see an error that port 800 is already in use:
   - Check if another instance of the server is running and stop it
   - Modify the port in `backend/server.py` (default is 8000)

2. **Permission Errors**
   If you encounter permission errors:
   - Ensure you have read/write permissions to the project directory
   - Run the command with appropriate privileges

3. **Missing Dependencies**
   This project uses only Python standard library modules, so no additional dependencies should be required.

4. **Frontend Not Loading**
   - Ensure the backend server is running
   - Check that the `frontend/` directory contains all HTML, CSS, and JS files
   - Verify that no firewall is blocking the connection

### Log Files

Server logs are written to `backend/logs/server.log`. Check this file for:
- Request information
- Error messages
- Startup and shutdown events

## Deployment

### Local Development

For local development:
1. Run the server as described above
2. Access the application at `http://localhost:8000`

### Production Deployment

For production deployment:
1. Ensure the server can be accessed on the desired port
2. Configure any necessary firewall rules
3. Consider running the server as a background service
4. Set up proper backup procedures for the data files in `backend/data/`

Note: This is a lightweight educational platform designed for simplicity. For production use with many concurrent users, consider adding a proper web server (like Nginx) as a reverse proxy and implementing additional security measures.

## Support

For issues, questions, or suggestions:
1. Check the server logs in `backend/logs/server.log`
2. Review this documentation
3. Open an issue in the repository or contact the project maintainers