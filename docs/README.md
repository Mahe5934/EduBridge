# EduBridge - Remote Learning System for Rural Colleges

## Project Overview

EduBridge is a lightweight remote learning system designed specifically for rural colleges with limited infrastructure. The platform connects rural college students with expert teachers and high-quality educational content through a lightweight, accessible system optimized for low-bandwidth environments.

The system consists of two main components:
1. **Backend**: A Python-based server using the built-in `http.server` module with a custom REST API
2. **Frontend**: A pure HTML/CSS/JavaScript interface with responsive design and offline capabilities

## Key Features

### For Students
- Access courses, lectures, notes, and quizzes from any device
- Download content for offline viewing in areas with limited connectivity
- Interactive quizzes with automatic grading and feedback
- Search functionality across all educational content
- Multi-language support for better accessibility

### For Educators
- Simple content management through JSON files
- RESTful API for programmatic access to educational resources
- No complex frameworks or dependencies to maintain
- Lightweight deployment on minimal hardware

### Technical Highlights
- **Lightweight Architecture**: Built with minimal dependencies for optimal performance in resource-constrained environments
- **Responsive Design**: Mobile-first approach with flexible layouts for all device sizes
- **Offline Capability**: Content can be downloaded for offline access
- **Security**: Input sanitization and file path validation to prevent security vulnerabilities
- **CORS Support**: Cross-origin resource sharing enabled for flexible frontend integration

## Project Structure

```
├── backend/
│   ├── api.py              # REST API endpoints implementation
│   ├── models.py           # Data models and structures
│   ├── server.py           # Main server implementation
│   ├── utils.py            # Utility functions and helpers
│   ├── data/               # JSON data storage
│   │   ├── courses.json
│   │   ├── lectures.json
│   │   ├── notes.json
│   │   └── quizzes.json
│   └── logs/
│       └── server.log      # Server activity logs
├── frontend/
│   ├── index.html          # Homepage
│   ├── about.html          # About page
│   ├── courses.html        # Courses listing
│   ├── course-detail.html  # Course details
│   ├── lecture.html        # Lecture viewing
│   ├── notes.html          # Course notes
│   ├── quiz.html           # Quiz interface
│   ├── search.html         # Search results
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # Client-side functionality
│   └── images/             # Static images and assets
└── docs/                   # Project documentation
    ├── README.md           # This file
    ├── Instructions.md     # Running instructions
    ├── backend/            # Backend documentation
    └── frontend/           # Frontend documentation
```

## Technology Stack

### Backend
- **Language**: Python 3.x
- **Framework**: Built-in `http.server` module (no external frameworks)
- **Data Storage**: JSON files
- **API**: RESTful endpoints with full CRUD operations
- **Security**: Input sanitization, file path validation, CORS support

### Frontend
- **Core Technologies**: HTML5, CSS3, JavaScript (ES6+)
- **Design**: Responsive layout with flexbox and grid
- **Interactivity**: Pure JavaScript with no external libraries
- **Compatibility**: Works on all modern browsers and gracefully degrades on older ones

## Getting Started

### Prerequisites
- Python 3.x installed on your system
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Quick Start
1. Clone or download the repository
2. Navigate to the project directory
3. Start the backend server:
   ```bash
   python backend/server.py
   ```
4. Open your browser and visit `http://localhost:8000`

For detailed installation and running instructions, please refer to:
- [General Instructions](Instructions.md)
- [Backend Documentation](backend/README_Backend.md)
- [Frontend Documentation](frontend/README_Frontend.md)

## API Endpoints

The backend provides RESTful API endpoints for all educational content:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/courses` | GET | Retrieve all courses |
| `/api/courses/{id}` | GET | Retrieve a specific course |
| `/api/courses` | POST | Create a new course |
| `/api/courses/{id}` | PUT | Update an existing course |
| `/api/courses/{id}` | DELETE | Delete a course |
| `/api/lectures` | GET | Retrieve all lectures |
| `/api/lectures/{id}` | GET | Retrieve a specific lecture |
| `/api/lectures` | POST | Create a new lecture |
| `/api/lectures/{id}` | PUT | Update an existing lecture |
| `/api/lectures/{id}` | DELETE | Delete a lecture |
| `/api/notes` | GET | Retrieve all notes |
| `/api/notes/{id}` | GET | Retrieve a specific note |
| `/api/notes` | POST | Create a new note |
| `/api/notes/{id}` | PUT | Update an existing note |
| `/api/notes/{id}` | DELETE | Delete a note |
| `/api/quizzes` | GET | Retrieve all quizzes |
| `/api/quizzes/{id}` | GET | Retrieve a specific quiz |
| `/api/quizzes` | POST | Create a new quiz |
| `/api/quizzes/{id}` | PUT | Update an existing quiz |
| `/api/quizzes/{id}` | DELETE | Delete a quiz |

## Contributing

This project is designed to be simple and maintainable. Contributions should focus on:
- Performance improvements
- Accessibility enhancements
- Mobile usability
- Lightweight solutions
- Offline functionality
- Multi-language support

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue in the repository or contact the project maintainers.