# EduBridge Frontend - Running Instructions

## Running the Application in VSCode with Live Server

### Prerequisites
1. Visual Studio Code installed on your system
2. Live Server extension installed in VSCode

### Steps to Run Using Live Server

1. **Open the Project in VSCode**
   - Launch Visual Studio Code
   - Open the project folder containing the frontend files
   - Navigate to File > Open Folder and select the project directory

2. **Install Live Server Extension**
   - Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X)
   - Search for "Live Server" by Ritwick Dey
   - Click Install

3. **Launch the Application**
   - Navigate to the `frontend` directory
   - Right-click on `index.html` file
   - Select "Open with Live Server" from the context menu
   - Alternatively, you can click "Go Live" button in the status bar at the bottom of VSCode

4. **Access the Application**
   - The application will automatically open in your default browser
   - The URL will typically be: `http://127.0.0.1:5500/frontend/index.html`
   - You can navigate between pages using the navigation menu

### Features Available in Live Server Mode
- Automatic browser refresh when files are modified
- Static file serving
- Cross-browser compatibility testing
- Local network access for testing on multiple devices

## Running the Application on a Production Server

### Using Python's Built-in HTTP Server

1. **Navigate to the Frontend Directory**
   ```bash
   cd frontend
   ```

2. **Start the Server**
   - For Python 3:
     ```bash
     python -m http.server 8000
     ```

3. **Access the Application**
   - Open your browser and navigate to `http://localhost:8080` (or the port shown in the terminal)

## Key Features of the EduBridge Frontend

1. **Fully Static Implementation**
   - No build process required
   - All HTML, CSS, and JavaScript files work directly in browsers
   - Minimal dependencies for easy deployment

2. **Responsive Design**
   - Works on desktop, tablet, and mobile devices
   - Adapts to different screen sizes

3. **Offline Capable**
   - Designed to work in low-bandwidth environments
   - Minimal asset sizes for faster loading

4. **Cross-Browser Compatibility**
   - Compatible with all modern browsers
   - Graceful degradation for older browsers

## Troubleshooting

### Common Issues and Solutions

1. **Live Server Not Starting**
   - Ensure no other application is using port 5500
   - Check if Windows Firewall is blocking the connection
   - Try changing the port in Live Server settings

2. **CSS Not Loading**
   - Verify that `css/style.css` exists in the correct location
   - Check browser developer tools for 404 errors
   - Ensure file paths in HTML files are correct

3. **JavaScript Functionality Not Working**
   - Check browser console for JavaScript errors
   - Verify that `js/main.js` exists and is properly linked
   - Ensure browser JavaScript is enabled

4. **Images Not Displaying**
   - Confirm that the `images` directory exists with required assets
   - Check file paths in HTML and CSS files
   - Verify image file formats are supported by browsers

### Browser Compatibility

The EduBridge frontend is designed to work with:
- Chrome (latest versions)
- Firefox (latest versions)
- Safari (latest versions)
- Microsoft Edge (latest versions)
- Mobile browsers (iOS Safari, Android Chrome)

For best results, use the latest version of your preferred browser.

## Development Notes

### File Structure
```
frontend/
├── index.html          # Homepage
├── about.html          # About page
├── courses.html        # Courses listing page
├── course-detail.html  # Course details page
├── lecture.html        # Lecture viewing page
├── notes.html          # Course notes page
├── quiz.html           # Quiz page
├── search.html         # Search results page
├── css/
│   └── style.css       # Main stylesheet
├── js/
│   └── main.js         # Main JavaScript file
└── images/
    ├── favicon.ico     # Site favicon
    └── [other images]  # Content images
```

### Customization
To customize the application:
1. Modify HTML files to change content
2. Update CSS in `css/style.css` to change styling
3. Add functionality by editing `js/main.js`
4. Add new pages by creating additional HTML files

Remember to test changes thoroughly after modifications.