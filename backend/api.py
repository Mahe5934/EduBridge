# =====================================================================================
# File: EduBridge/backend/api.py
# Description: API handler for EduBridge backend
# Created: 2025-09-16 12:00:00
# Last Modified: 2025-09-16 12:00:00
# =====================================================================================

import json
import os
import logging
from typing import Dict, Any, List, Optional
from http import HTTPStatus

# Import our modules
from utils import load_json_data, save_json_data, generate_id, APIError, handle_api_error
from models import create_model_instance, get_model_class

# Configure logger
logger = logging.getLogger(__name__)

class APIHandler:
    """Handler for API endpoints"""
    
    def __init__(self):
        """Initialize API handler"""
        self.data_dir = 'backend/data'
        # Ensure data directory exists
        os.makedirs(self.data_dir, exist_ok=True)
    
    def handle_get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle GET requests
        
        Args:
            path: API endpoint path
            params: Query parameters
            
        Returns:
            API response dictionary
        """
        try:
            logger.info(f"Handling GET request for {path}")
            
            # Remove /api prefix if present
            if path.startswith('/api'):
                path = path[4:]  # Remove /api prefix
            
            # Route to appropriate handler based on path
            if path.startswith('/courses'):
                return self._handle_get_courses(path, params)
            elif path.startswith('/lectures'):
                return self._handle_get_lectures(path, params)
            elif path.startswith('/notes'):
                return self._handle_get_notes(path, params)
            elif path.startswith('/quizzes'):
                return self._handle_get_quizzes(path, params)
            else:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Endpoint not found'
                }
        except Exception as e:
            logger.error(f"Error handling GET request for {path}: {e}", exc_info=True)
            return handle_api_error(e)
    
    def handle_post(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle POST requests
        
        Args:
            path: API endpoint path
            data: Request data
            
        Returns:
            API response dictionary
        """
        try:
            logger.info(f"Handling POST request for {path}")
            
            # Remove /api prefix if present
            if path.startswith('/api'):
                path = path[4:]  # Remove /api prefix
            
            # Route to appropriate handler based on path
            if path.startswith('/courses'):
                return self._handle_create_course(data)
            elif path.startswith('/lectures'):
                return self._handle_create_lecture(data)
            elif path.startswith('/notes'):
                return self._handle_create_note(data)
            elif path.startswith('/quizzes'):
                return self._handle_create_quiz(data)
            else:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Endpoint not found'
                }
        except Exception as e:
            logger.error(f"Error handling POST request for {path}: {e}", exc_info=True)
            return handle_api_error(e)
    
    def handle_put(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle PUT requests
        
        Args:
            path: API endpoint path
            data: Request data
            
        Returns:
            API response dictionary
        """
        try:
            logger.info(f"Handling PUT request for {path}")
            
            # Remove /api prefix if present
            if path.startswith('/api'):
                path = path[4:]  # Remove /api prefix
            
            # Route to appropriate handler based on path
            if path.startswith('/courses/'):
                return self._handle_update_course(path, data)
            elif path.startswith('/lectures/'):
                return self._handle_update_lecture(path, data)
            elif path.startswith('/notes/'):
                return self._handle_update_note(path, data)
            elif path.startswith('/quizzes/'):
                return self._handle_update_quiz(path, data)
            else:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Endpoint not found'
                }
        except Exception as e:
            logger.error(f"Error handling PUT request for {path}: {e}", exc_info=True)
            return handle_api_error(e)
    
    def handle_delete(self, path: str) -> Dict[str, Any]:
        """
        Handle DELETE requests
        
        Args:
            path: API endpoint path
            
        Returns:
            API response dictionary
        """
        try:
            logger.info(f"Handling DELETE request for {path}")
            
            # Remove /api prefix if present
            if path.startswith('/api'):
                path = path[4:]  # Remove /api prefix
            
            # Route to appropriate handler based on path
            if path.startswith('/courses/'):
                return self._handle_delete_course(path)
            elif path.startswith('/lectures/'):
                return self._handle_delete_lecture(path)
            elif path.startswith('/notes/'):
                return self._handle_delete_note(path)
            elif path.startswith('/quizzes/'):
                return self._handle_delete_quiz(path)
            else:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Endpoint not found'
                }
        except Exception as e:
            logger.error(f"Error handling DELETE request for {path}: {e}", exc_info=True)
            return handle_api_error(e)
    
    # === Course handlers ===
    
    def _handle_get_courses(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle GET requests for courses"""
        try:
            # Get all courses
            courses_file = os.path.join(self.data_dir, 'courses.json')
            courses = load_json_data(courses_file)
            
            # If requesting a specific course
            if path.startswith('/courses/'):
                course_id = path.split('/')[2] if len(path.split('/')) > 2 else None
                if course_id:
                    course = next((c for c in courses if c['id'] == course_id), None)
                    if course:
                        return {
                            'status': HTTPStatus.OK,
                            'data': course
                        }
                    else:
                        return {
                            'status': HTTPStatus.NOT_FOUND,
                            'error': 'Course not found'
                        }
            
            # Return all courses
            return {
                'status': HTTPStatus.OK,
                'data': courses
            }
        except Exception as e:
            logger.error(f"Error getting courses: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_create_course(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle POST requests to create a course"""
        try:
            # Validate required fields
            required_fields = ['title', 'description', 'category']
            for field in required_fields:
                if field not in data or not data[field]:
                    return {
                        'status': HTTPStatus.BAD_REQUEST,
                        'error': f'Missing required field: {field}'
                    }
            
            # Create course object
            course_data = {
                'id': generate_id(),
                'title': data['title'],
                'description': data['description'],
                'category': data['category'],
                'duration': data.get('duration', 0),
                'lectures_count': data.get('lectures_count', 0),
                'instructor': data.get('instructor', ''),
                'thumbnail': data.get('thumbnail', ''),
                'level': data.get('level', 'Beginner')
            }
            
            # Load existing courses
            courses_file = os.path.join(self.data_dir, 'courses.json')
            courses = load_json_data(courses_file)
            
            # Add new course
            courses.append(course_data)
            
            # Save courses
            if save_json_data(courses_file, courses):
                return {
                    'status': HTTPStatus.CREATED,
                    'data': course_data
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to save course'
                }
        except Exception as e:
            logger.error(f"Error creating course: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_update_course(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle PUT requests to update a course"""
        try:
            # Extract course ID from path
            course_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not course_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Course ID is required'
                }
            
            # Load existing courses
            courses_file = os.path.join(self.data_dir, 'courses.json')
            courses = load_json_data(courses_file)
            
            # Find course to update
            course_index = None
            for i, course in enumerate(courses):
                if course['id'] == course_id:
                    course_index = i
                    break
            
            if course_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Course not found'
                }
            
            # Update course fields
            course = courses[course_index]
            updatable_fields = ['title', 'description', 'category', 'duration', 'lectures_count', 'instructor', 'thumbnail', 'level']
            for field in updatable_fields:
                if field in data:
                    course[field] = data[field]
            
            # Update timestamp
            course['updated_at'] = self._get_current_timestamp()
            
            # Save courses
            if save_json_data(courses_file, courses):
                return {
                    'status': HTTPStatus.OK,
                    'data': course
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to update course'
                }
        except Exception as e:
            logger.error(f"Error updating course: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_delete_course(self, path: str) -> Dict[str, Any]:
        """Handle DELETE requests to delete a course"""
        try:
            # Extract course ID from path
            course_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not course_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Course ID is required'
                }
            
            # Load existing courses
            courses_file = os.path.join(self.data_dir, 'courses.json')
            courses = load_json_data(courses_file)
            
            # Find course to delete
            course_index = None
            for i, course in enumerate(courses):
                if course['id'] == course_id:
                    course_index = i
                    break
            
            if course_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Course not found'
                }
            
            # Remove course
            deleted_course = courses.pop(course_index)
            
            # Save courses
            if save_json_data(courses_file, courses):
                return {
                    'status': HTTPStatus.OK,
                    'data': deleted_course
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to delete course'
                }
        except Exception as e:
            logger.error(f"Error deleting course: {e}", exc_info=True)
            return handle_api_error(e)
    
    # === Lecture handlers ===
    
    def _handle_get_lectures(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle GET requests for lectures"""
        try:
            # Get all lectures
            lectures_file = os.path.join(self.data_dir, 'lectures.json')
            lectures = load_json_data(lectures_file)
            
            # Filter by course_id if provided
            course_id = params.get('course_id')
            if course_id:
                lectures = [l for l in lectures if l.get('course_id') == course_id]
            
            # If requesting a specific lecture
            if path.startswith('/lectures/'):
                lecture_id = path.split('/')[2] if len(path.split('/')) > 2 else None
                if lecture_id:
                    lecture = next((l for l in lectures if l['id'] == lecture_id), None)
                    if lecture:
                        return {
                            'status': HTTPStatus.OK,
                            'data': lecture
                        }
                    else:
                        return {
                            'status': HTTPStatus.NOT_FOUND,
                            'error': 'Lecture not found'
                        }
            
            # Return lectures
            return {
                'status': HTTPStatus.OK,
                'data': lectures
            }
        except Exception as e:
            logger.error(f"Error getting lectures: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_create_lecture(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle POST requests to create a lecture"""
        try:
            # Validate required fields
            required_fields = ['course_id', 'title', 'description', 'video_url']
            for field in required_fields:
                if field not in data or not data[field]:
                    return {
                        'status': HTTPStatus.BAD_REQUEST,
                        'error': f'Missing required field: {field}'
                    }
            
            # Create lecture object
            lecture_data = {
                'id': generate_id(),
                'course_id': data['course_id'],
                'title': data['title'],
                'description': data['description'],
                'duration': data.get('duration', 0),
                'video_url': data['video_url'],
                'order': data.get('order', 0)
            }
            
            # Load existing lectures
            lectures_file = os.path.join(self.data_dir, 'lectures.json')
            lectures = load_json_data(lectures_file)
            
            # Add new lecture
            lectures.append(lecture_data)
            
            # Save lectures
            if save_json_data(lectures_file, lectures):
                return {
                    'status': HTTPStatus.CREATED,
                    'data': lecture_data
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to save lecture'
                }
        except Exception as e:
            logger.error(f"Error creating lecture: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_update_lecture(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle PUT requests to update a lecture"""
        try:
            # Extract lecture ID from path
            lecture_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not lecture_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Lecture ID is required'
                }
            
            # Load existing lectures
            lectures_file = os.path.join(self.data_dir, 'lectures.json')
            lectures = load_json_data(lectures_file)
            
            # Find lecture to update
            lecture_index = None
            for i, lecture in enumerate(lectures):
                if lecture['id'] == lecture_id:
                    lecture_index = i
                    break
            
            if lecture_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Lecture not found'
                }
            
            # Update lecture fields
            lecture = lectures[lecture_index]
            updatable_fields = ['course_id', 'title', 'description', 'duration', 'video_url', 'order']
            for field in updatable_fields:
                if field in data:
                    lecture[field] = data[field]
            
            # Update timestamp
            lecture['updated_at'] = self._get_current_timestamp()
            
            # Save lectures
            if save_json_data(lectures_file, lectures):
                return {
                    'status': HTTPStatus.OK,
                    'data': lecture
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to update lecture'
                }
        except Exception as e:
            logger.error(f"Error updating lecture: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_delete_lecture(self, path: str) -> Dict[str, Any]:
        """Handle DELETE requests to delete a lecture"""
        try:
            # Extract lecture ID from path
            lecture_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not lecture_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Lecture ID is required'
                }
            
            # Load existing lectures
            lectures_file = os.path.join(self.data_dir, 'lectures.json')
            lectures = load_json_data(lectures_file)
            
            # Find lecture to delete
            lecture_index = None
            for i, lecture in enumerate(lectures):
                if lecture['id'] == lecture_id:
                    lecture_index = i
                    break
            
            if lecture_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Lecture not found'
                }
            
            # Remove lecture
            deleted_lecture = lectures.pop(lecture_index)
            
            # Save lectures
            if save_json_data(lectures_file, lectures):
                return {
                    'status': HTTPStatus.OK,
                    'data': deleted_lecture
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to delete lecture'
                }
        except Exception as e:
            logger.error(f"Error deleting lecture: {e}", exc_info=True)
            return handle_api_error(e)
    
    # === Note handlers ===
    
    def _handle_get_notes(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle GET requests for notes"""
        try:
            # Get all notes
            notes_file = os.path.join(self.data_dir, 'notes.json')
            notes = load_json_data(notes_file)
            
            # Filter by course_id or lecture_id if provided
            course_id = params.get('course_id')
            lecture_id = params.get('lecture_id')
            
            if course_id:
                notes = [n for n in notes if n.get('course_id') == course_id]
            if lecture_id:
                notes = [n for n in notes if n.get('lecture_id') == lecture_id]
            
            # If requesting a specific note
            if path.startswith('/notes/'):
                note_id = path.split('/')[2] if len(path.split('/')) > 2 else None
                if note_id:
                    note = next((n for n in notes if n['id'] == note_id), None)
                    if note:
                        return {
                            'status': HTTPStatus.OK,
                            'data': note
                        }
                    else:
                        return {
                            'status': HTTPStatus.NOT_FOUND,
                            'error': 'Note not found'
                        }
            
            # Return notes
            return {
                'status': HTTPStatus.OK,
                'data': notes
            }
        except Exception as e:
            logger.error(f"Error getting notes: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_create_note(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle POST requests to create a note"""
        try:
            # Validate required fields
            required_fields = ['course_id', 'lecture_id', 'title', 'content']
            for field in required_fields:
                if field not in data or not data[field]:
                    return {
                        'status': HTTPStatus.BAD_REQUEST,
                        'error': f'Missing required field: {field}'
                    }
            
            # Create note object
            note_data = {
                'id': generate_id(),
                'course_id': data['course_id'],
                'lecture_id': data['lecture_id'],
                'title': data['title'],
                'content': data['content'],
                'file_url': data.get('file_url', '')
            }
            
            # Load existing notes
            notes_file = os.path.join(self.data_dir, 'notes.json')
            notes = load_json_data(notes_file)
            
            # Add new note
            notes.append(note_data)
            
            # Save notes
            if save_json_data(notes_file, notes):
                return {
                    'status': HTTPStatus.CREATED,
                    'data': note_data
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to save note'
                }
        except Exception as e:
            logger.error(f"Error creating note: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_update_note(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle PUT requests to update a note"""
        try:
            # Extract note ID from path
            note_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not note_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Note ID is required'
                }
            
            # Load existing notes
            notes_file = os.path.join(self.data_dir, 'notes.json')
            notes = load_json_data(notes_file)
            
            # Find note to update
            note_index = None
            for i, note in enumerate(notes):
                if note['id'] == note_id:
                    note_index = i
                    break
            
            if note_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Note not found'
                }
            
            # Update note fields
            note = notes[note_index]
            updatable_fields = ['course_id', 'lecture_id', 'title', 'content', 'file_url']
            for field in updatable_fields:
                if field in data:
                    note[field] = data[field]
            
            # Update timestamp
            note['updated_at'] = self._get_current_timestamp()
            
            # Save notes
            if save_json_data(notes_file, notes):
                return {
                    'status': HTTPStatus.OK,
                    'data': note
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to update note'
                }
        except Exception as e:
            logger.error(f"Error updating note: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_delete_note(self, path: str) -> Dict[str, Any]:
        """Handle DELETE requests to delete a note"""
        try:
            # Extract note ID from path
            note_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not note_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Note ID is required'
                }
            
            # Load existing notes
            notes_file = os.path.join(self.data_dir, 'notes.json')
            notes = load_json_data(notes_file)
            
            # Find note to delete
            note_index = None
            for i, note in enumerate(notes):
                if note['id'] == note_id:
                    note_index = i
                    break
            
            if note_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Note not found'
                }
            
            # Remove note
            deleted_note = notes.pop(note_index)
            
            # Save notes
            if save_json_data(notes_file, notes):
                return {
                    'status': HTTPStatus.OK,
                    'data': deleted_note
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to delete note'
                }
        except Exception as e:
            logger.error(f"Error deleting note: {e}", exc_info=True)
            return handle_api_error(e)
    
    # === Quiz handlers ===
    
    def _handle_get_quizzes(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle GET requests for quizzes"""
        try:
            # Get all quizzes
            quizzes_file = os.path.join(self.data_dir, 'quizzes.json')
            quizzes = load_json_data(quizzes_file)
            
            # Filter by course_id or lecture_id if provided
            course_id = params.get('course_id')
            lecture_id = params.get('lecture_id')
            
            if course_id:
                quizzes = [q for q in quizzes if q.get('course_id') == course_id]
            if lecture_id:
                quizzes = [q for q in quizzes if q.get('lecture_id') == lecture_id]
            
            # If requesting a specific quiz
            if path.startswith('/quizzes/'):
                quiz_id = path.split('/')[2] if len(path.split('/')) > 2 else None
                if quiz_id:
                    quiz = next((q for q in quizzes if q['id'] == quiz_id), None)
                    if quiz:
                        return {
                            'status': HTTPStatus.OK,
                            'data': quiz
                        }
                    else:
                        return {
                            'status': HTTPStatus.NOT_FOUND,
                            'error': 'Quiz not found'
                        }
            
            # Return quizzes
            return {
                'status': HTTPStatus.OK,
                'data': quizzes
            }
        except Exception as e:
            logger.error(f"Error getting quizzes: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_create_quiz(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle POST requests to create a quiz"""
        try:
            # Validate required fields
            required_fields = ['course_id', 'lecture_id', 'title']
            for field in required_fields:
                if field not in data or not data[field]:
                    return {
                        'status': HTTPStatus.BAD_REQUEST,
                        'error': f'Missing required field: {field}'
                    }
            
            # Create quiz object
            quiz_data = {
                'id': generate_id(),
                'course_id': data['course_id'],
                'lecture_id': data['lecture_id'],
                'title': data['title'],
                'questions': data.get('questions', [])
            }
            
            # Load existing quizzes
            quizzes_file = os.path.join(self.data_dir, 'quizzes.json')
            quizzes = load_json_data(quizzes_file)
            
            # Add new quiz
            quizzes.append(quiz_data)
            
            # Save quizzes
            if save_json_data(quizzes_file, quizzes):
                return {
                    'status': HTTPStatus.CREATED,
                    'data': quiz_data
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to save quiz'
                }
        except Exception as e:
            logger.error(f"Error creating quiz: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_update_quiz(self, path: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle PUT requests to update a quiz"""
        try:
            # Extract quiz ID from path
            quiz_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not quiz_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Quiz ID is required'
                }
            
            # Load existing quizzes
            quizzes_file = os.path.join(self.data_dir, 'quizzes.json')
            quizzes = load_json_data(quizzes_file)
            
            # Find quiz to update
            quiz_index = None
            for i, quiz in enumerate(quizzes):
                if quiz['id'] == quiz_id:
                    quiz_index = i
                    break
            
            if quiz_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Quiz not found'
                }
            
            # Update quiz fields
            quiz = quizzes[quiz_index]
            updatable_fields = ['course_id', 'lecture_id', 'title', 'questions']
            for field in updatable_fields:
                if field in data:
                    quiz[field] = data[field]
            
            # Update timestamp
            quiz['updated_at'] = self._get_current_timestamp()
            
            # Save quizzes
            if save_json_data(quizzes_file, quizzes):
                return {
                    'status': HTTPStatus.OK,
                    'data': quiz
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to update quiz'
                }
        except Exception as e:
            logger.error(f"Error updating quiz: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _handle_delete_quiz(self, path: str) -> Dict[str, Any]:
        """Handle DELETE requests to delete a quiz"""
        try:
            # Extract quiz ID from path
            quiz_id = path.split('/')[2] if len(path.split('/')) > 2 else None
            if not quiz_id:
                return {
                    'status': HTTPStatus.BAD_REQUEST,
                    'error': 'Quiz ID is required'
                }
            
            # Load existing quizzes
            quizzes_file = os.path.join(self.data_dir, 'quizzes.json')
            quizzes = load_json_data(quizzes_file)
            
            # Find quiz to delete
            quiz_index = None
            for i, quiz in enumerate(quizzes):
                if quiz['id'] == quiz_id:
                    quiz_index = i
                    break
            
            if quiz_index is None:
                return {
                    'status': HTTPStatus.NOT_FOUND,
                    'error': 'Quiz not found'
                }
            
            # Remove quiz
            deleted_quiz = quizzes.pop(quiz_index)
            
            # Save quizzes
            if save_json_data(quizzes_file, quizzes):
                return {
                    'status': HTTPStatus.OK,
                    'data': deleted_quiz
                }
            else:
                return {
                    'status': HTTPStatus.INTERNAL_SERVER_ERROR,
                    'error': 'Failed to delete quiz'
                }
        except Exception as e:
            logger.error(f"Error deleting quiz: {e}", exc_info=True)
            return handle_api_error(e)
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp in ISO format"""
        from datetime import datetime
        return datetime.now().isoformat()