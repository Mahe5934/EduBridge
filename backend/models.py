# =====================================================================================
# File: EduBridge/backend/models.py
# Description: Data models for EduBridge backend
# Created: 2025-09-16 10:25:35
# Last Modified: 2025-09-16 10:25:35
# =====================================================================================

import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class BaseModel:
    """Base model class with common functionality"""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary"""
        return asdict(self)
    
    def to_json(self) -> str:
        """Convert model to JSON string"""
        return json.dumps(self.to_dict(), indent=2)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        """Create model instance from dictionary"""
        return cls(**data)

@dataclass
class Course(BaseModel):
    """Course model"""
    id: str
    title: str
    description: str
    category: str
    duration: int  # in hours
    lectures_count: int
    created_at: str
    updated_at: str
    instructor: str = ""
    thumbnail: str = ""
    level: str = "Beginner"
    
    def __post_init__(self):
        # Set default timestamps if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

@dataclass
class Lecture(BaseModel):
    """Lecture model"""
    id: str
    course_id: str
    title: str
    description: str
    duration: int  # in minutes
    video_url: str
    order: int
    created_at: str
    updated_at: str
    
    def __post_init__(self):
        # Set default timestamps if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

@dataclass
class Note(BaseModel):
    """Note model"""
    id: str
    course_id: str
    lecture_id: str
    title: str
    content: str
    created_at: str
    updated_at: str
    file_url: str = ""
    
    def __post_init__(self):
        # Set default timestamps if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

@dataclass
class Quiz(BaseModel):
    """Quiz model"""
    id: str
    course_id: str
    lecture_id: str
    title: str
    questions: List[Dict[str, Any]]  # List of question objects
    created_at: str
    updated_at: str
    
    def __post_init__(self):
        # Set default timestamps if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

@dataclass
class Question(BaseModel):
    """Question model for quizzes"""
    id: str
    quiz_id: str
    text: str
    options: List[str]
    correct_answer: int  # Index of correct answer in options list
    explanation: str
    created_at: str
    updated_at: str
    
    def __post_init__(self):
        # Set default timestamps if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

@dataclass
class User(BaseModel):
    """User model for admin authentication"""
    id: str
    username: str
    password_hash: str  # Store hashed password, never plain text
    role: str  # admin, instructor, student
    created_at: str
    updated_at: str
    
    def __post_init__(self):
        # Set default timestamps if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

@dataclass
class SearchIndex(BaseModel):
    """Search index model for content search"""
    id: str
    content_type: str  # course, lecture, note, quiz
    content_id: str
    title: str
    description: str
    category: str
    tags: List[str]
    created_at: str
    
    def __post_init__(self):
        # Set default timestamp if not provided
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

# Model registry for easy access
MODEL_REGISTRY = {
    'course': Course,
    'lecture': Lecture,
    'note': Note,
    'quiz': Quiz,
    'question': Question,
    'user': User,
    'search_index': SearchIndex
}

def get_model_class(model_name: str) -> BaseModel:
    """Get model class by name"""
    return MODEL_REGISTRY.get(model_name.lower())

def create_model_instance(model_name: str, data: Dict[str, Any]) -> BaseModel:
    """Create model instance from data"""
    model_class = get_model_class(model_name)
    if not model_class:
        raise ValueError(f"Unknown model: {model_name}")
    
    # Filter data to only include fields that exist in the model
    model_fields = model_class.__annotations__.keys()
    filtered_data = {k: v for k, v in data.items() if k in model_fields}
    
    return model_class(**filtered_data)