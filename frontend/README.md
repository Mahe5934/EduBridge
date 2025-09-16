# EduBridge Frontend

This directory contains the frontend implementation for the EduBridge project, a lightweight remote learning system designed for rural colleges with limited infrastructure.

## Project Overview

EduBridge connects rural college students with expert teachers and educational resources through a simple web interface. The frontend is built with plain HTML, CSS, and JavaScript to ensure low-bandwidth optimization and accessibility.

## Directory Structure

```
frontend/
├── index.html          # Homepage
├── about.html          # About page
├── courses.html        # Courses listing page
├── css/
│   └── style.css       # Main stylesheet
├── js/
│   └── main.js         # Main JavaScript file
└── images/
    ├── favicon.ico     # Site favicon
    └── placeholder.txt # Placeholder for images directory
```

## Features

1. **Responsive Design**: Works on desktop, tablet, and mobile devices
2. **Lightweight**: Optimized for low-bandwidth rural internet connections
3. **Accessible**: Clean, simple interface suitable for first-time digital learners
4. **Navigation**: Consistent header and footer navigation across all pages
5. **Course Filtering**: Ability to search and filter courses by category
6. **Mobile Menu**: Collapsible navigation menu for small screens

## Pages

### Homepage (index.html)
- Project overview and introduction
- Key features highlighting the benefits of EduBridge
- Call-to-action to explore courses

### About Page (about.html)
- Detailed information about the EduBridge mission
- Challenges faced by rural colleges
- How EduBridge addresses these challenges

### Courses Page (courses.html)
- Catalog of available courses
- Search and filtering functionality
- Course cards with descriptions and metadata

## Technical Implementation

### CSS Features
- Mobile-first responsive design
- CSS Grid and Flexbox for layouts
- CSS animations for interactive elements
- Optimized for performance with minimal CSS

### JavaScript Features
- Mobile menu toggle functionality
- Course filtering and search
- Smooth scrolling for anchor links
- Form validation utilities
- Performance optimizations (debouncing)
- Lazy loading preparation

## Optimization for Rural Environments

1. **Minimal Dependencies**: No external libraries or frameworks
2. **Lightweight Assets**: CSS and JS files are kept small
3. **Efficient Code**: Clean, optimized code structure
4. **Progressive Enhancement**: Core functionality works without JavaScript
5. **Responsive Images**: Images are sized appropriately for different devices

## How to Run

1. Simply open any of the HTML files in a web browser
2. No build process or server required
3. All pages are statically linked and work independently

## Browser Support

The frontend is designed to work on all modern browsers including:
- Chrome
- Firefox
- Safari
- Edge
- Mobile browsers

## Future Enhancements

1. Add actual course content and lecture pages
2. Implement user authentication
3. Add offline functionality with service workers
4. Include multi-language support
5. Add interactive quizzes and assessments

## Development Guidelines

1. Keep all code lightweight and performant
2. Maintain consistency in design and navigation
3. Ensure accessibility standards are met
4. Test on multiple devices and browsers
5. Optimize for low-bandwidth scenarios

## Contributing

This project is part of a 3-month implementation plan for rural college education. Contributions should focus on:
- Performance improvements
- Accessibility enhancements
- Mobile usability
- Lightweight solutions