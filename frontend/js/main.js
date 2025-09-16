/*
=====================================================================================
File: EduBridge/frontend/js/main.js
Description: Main JavaScript file for EduBridge frontend interactivity
Created: 2025-09-16 09:38:01
Last Modified: 2025-09-16 09:58:30
=====================================================================================
*/

// DOM Content Loaded Event
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive components
    initMobileMenu();
    initCourseFiltering();
    initSmoothScrolling();
    initSearchFunctionality();
    initQuizFunctionality();
    initVideoPlayer();
});

// Mobile Menu Toggle
function initMobileMenu() {
    const menuToggle = document.createElement('div');
    menuToggle.className = 'menu-toggle';
    menuToggle.innerHTML = '☰';
    menuToggle.setAttribute('aria-label', 'Toggle navigation menu');
    
    const headerContainer = document.querySelector('header .container');
    const nav = document.querySelector('nav');
    
    if (headerContainer && nav) {
        headerContainer.insertBefore(menuToggle, nav);
        
        menuToggle.addEventListener('click', function() {
            const navUl = nav.querySelector('ul');
            navUl.classList.toggle('show');
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            const navUl = nav.querySelector('ul');
            if (!nav.contains(event.target) && !menuToggle.contains(event.target)) {
                navUl.classList.remove('show');
            }
        });
    }
}

// Course Filtering Functionality
function initCourseFiltering() {
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    const searchBtn = document.getElementById('searchBtn');
    const courseCards = document.querySelectorAll('.course-card');
    
    if (searchInput && categoryFilter && searchBtn && courseCards.length > 0) {
        // Search button event
        searchBtn.addEventListener('click', filterCourses);
        
        // Enter key in search input
        searchInput.addEventListener('keyup', function(event) {
            if (event.key === 'Enter') {
                filterCourses();
            }
        });
        
        // Category filter change
        categoryFilter.addEventListener('change', filterCourses);
    }
    
    // Enhanced filtering for courses page
    const sortFilter = document.getElementById('sortFilter');
    const clearSearchBtn = document.getElementById('clearSearchBtn');
    const clearFiltersBtn = document.getElementById('clearFiltersBtn');
    
    if (sortFilter) {
        sortFilter.addEventListener('change', function() {
            sortCourses();
            filterCourses();
        });
    }
    
    if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', function() {
            if (searchInput) {
                searchInput.value = '';
                filterCourses();
            }
        });
    }
    
    if (clearFiltersBtn) {
        clearFiltersBtn.addEventListener('click', function() {
            if (searchInput) searchInput.value = '';
            if (categoryFilter) categoryFilter.value = 'all';
            if (sortFilter) sortFilter.value = 'popular';
            filterCourses();
        });
    }
    
    // Show clear button when search input has content
    if (searchInput && clearSearchBtn) {
        searchInput.addEventListener('input', function() {
            clearSearchBtn.style.display = searchInput.value ? 'block' : 'none';
        });
    }
}

// Filter courses based on search input and category
function filterCourses() {
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    
    const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedCategory = categoryFilter ? categoryFilter.value : 'all';
    
    const courseCards = document.querySelectorAll('.course-card');
    let visibleCount = 0;
    
    courseCards.forEach(card => {
        const title = card.querySelector('h3').textContent.toLowerCase();
        const category = card.querySelector('.course-category').textContent.toLowerCase();
        const description = card.querySelector('p').textContent.toLowerCase();
        
        const matchesSearch = searchTerm === '' || 
                             title.includes(searchTerm) || 
                             description.includes(searchTerm);
        
        const matchesCategory = selectedCategory === 'all' || 
                               category.includes(selectedCategory);
        
        if (matchesSearch && matchesCategory) {
            card.style.display = 'block';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });
    
    // Update active filters count
    updateActiveFiltersCount(visibleCount);
    
    // Show/hide clear filters button
    const clearFiltersBtn = document.getElementById('clearFiltersBtn');
    const hasFilters = searchTerm !== '' || selectedCategory !== 'all';
    if (clearFiltersBtn) {
        clearFiltersBtn.style.display = hasFilters ? 'inline-block' : 'none';
    }
}

// Sort courses
function sortCourses() {
    const sortFilter = document.getElementById('sortFilter');
    const courseGrid = document.querySelector('.course-grid');
    
    if (!sortFilter || !courseGrid) return;
    
    const sortBy = sortFilter.value;
    const courseCards = document.querySelectorAll('.course-card');
    
    // Convert NodeList to Array for sorting
    const cardsArray = Array.from(courseCards);
    
    // Sort based on selected option
    cardsArray.sort((a, b) => {
        const titleA = a.querySelector('h3').textContent.toLowerCase();
        const titleB = b.querySelector('h3').textContent.toLowerCase();
        const durationA = parseInt(a.querySelector('.duration').textContent) || 0;
        const durationB = parseInt(b.querySelector('.duration').textContent) || 0;
        
        switch (sortBy) {
            case 'a-z':
                return titleA.localeCompare(titleB);
            case 'z-a':
                return titleB.localeCompare(titleA);
            case 'duration':
                return durationA - durationB;
            case 'newest':
                // For demo purposes, we'll reverse the order
                return Array.from(courseCards).indexOf(b) - Array.from(courseCards).indexOf(a);
            default: // popular
                // For demo purposes, we'll keep the original order
                return Array.from(courseCards).indexOf(a) - Array.from(courseCards).indexOf(b);
        }
    });
    
    // Re-append sorted cards to the grid
    cardsArray.forEach(card => {
        courseGrid.appendChild(card);
    });
}

// Update active filters count
function updateActiveFiltersCount(count) {
    const activeFiltersCount = document.getElementById('activeFiltersCount');
    const courseCards = document.querySelectorAll('.course-card');
    
    if (!activeFiltersCount) return;
    
    if (count !== undefined) {
        activeFiltersCount.textContent = `Showing ${count} of ${courseCards.length} courses`;
    } else {
        // Count visible courses
        const visibleCourses = Array.from(courseCards).filter(card => 
            card.style.display !== 'none'
        ).length;
        activeFiltersCount.textContent = `Showing ${visibleCourses} of ${courseCards.length} courses`;
    }
}

// Smooth Scrolling for Anchor Links
function initSmoothScrolling() {
    // Get all anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Check if it's an internal anchor link
            const targetId = this.getAttribute('href');
            if (targetId !== '#' && targetId.startsWith('#')) {
                e.preventDefault();
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    // Scroll to the element with smooth behavior
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}

// Form Validation for Any Future Forms
function validateForm(form) {
    const inputs = form.querySelectorAll('input, textarea, select');
    let isValid = true;
    
    inputs.forEach(input => {
        // Reset previous error states
        input.classList.remove('error');
        
        // Check for required fields
        if (input.hasAttribute('required') && !input.value.trim()) {
            input.classList.add('error');
            isValid = false;
        }
        
        // Check for email validation
        if (input.type === 'email' && input.value.trim()) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(input.value.trim())) {
                input.classList.add('error');
                isValid = false;
            }
        }
    });
    
    return isValid;
}

// Lazy Loading for Images (for future implementation)
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for browsers that don't support Intersection Observer
        images.forEach(img => {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        });
    }
}

// Performance optimized debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Simple animation for elements when they come into view
function initScrollAnimations() {
    const animateOnScroll = debounce(function() {
        const elements = document.querySelectorAll('.feature-card, .step, .course-card');
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('animated');
            }
        });
    }, 100);
    
    // Initial check
    animateOnScroll();
    
    // Add scroll event listener
    window.addEventListener('scroll', animateOnScroll);
}

// Add simple CSS for animations (in case it's not in the CSS file)
function addAnimationStyles() {
    const style = document.createElement('style');
    style.textContent = `
        .feature-card, .step, .course-card {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        .feature-card.animated, .step.animated, .course-card.animated {
            opacity: 1;
            transform: translateY(0);
        }
    `;
    document.head.appendChild(style);
}

// Initialize all functionality when the page loads
window.addEventListener('load', function() {
    // Add animation styles
    addAnimationStyles();
    
    // Initialize scroll animations
    initScrollAnimations();
    
    // Initialize lazy loading if there are images with data-src
    if (document.querySelectorAll('img[data-src]').length > 0) {
        initLazyLoading();
    }
});

// Utility function to get URL parameters
function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    const results = regex.exec(window.location.href);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

// Utility function to set a cookie
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

// Utility function to get a cookie
function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Search functionality for search page
function initSearchFunctionality() {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    const contentTypeFilter = document.getElementById('contentTypeFilter');
    const categoryFilter = document.getElementById('categoryFilter');
    
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            performSearch();
        });
    }
    
    if (searchInput) {
        searchInput.addEventListener('keyup', function(e) {
            if (e.key === 'Enter') {
                performSearch();
            }
        });
    }
    
    if (contentTypeFilter) {
        contentTypeFilter.addEventListener('change', performSearch);
    }
    
    if (categoryFilter) {
        categoryFilter.addEventListener('change', performSearch);
    }
}

// Perform search across content
function performSearch() {
    const searchInput = document.getElementById('searchInput');
    const contentTypeFilter = document.getElementById('contentTypeFilter');
    const categoryFilter = document.getElementById('categoryFilter');
    
    if (!searchInput) return;
    
    const searchTerm = searchInput.value.toLowerCase().trim();
    const contentType = contentTypeFilter ? contentTypeFilter.value : 'all';
    const category = categoryFilter ? categoryFilter.value : 'all';
    
    // In a real implementation, this would call an API or filter existing content
    console.log('Performing search:', { searchTerm, contentType, category });
    
    // For demonstration, we'll just show an alert
    if (searchTerm) {
        alert(`Searching for: ${searchTerm}\nContent Type: ${contentType}\nCategory: ${category}`);
    }
}

// Quiz functionality
function initQuizFunctionality() {
    const quizForm = document.getElementById('quizForm');
    const submitQuizBtn = document.getElementById('submitQuizBtn');
    const resetQuizBtn = document.getElementById('resetQuizBtn');
    const timerElement = document.getElementById('timer');
    
    // Quiz answers (in a real implementation, these would come from a database)
    const correctAnswers = {
        q1: 'c',
        q2: 'b',
        q3: 'c',
        q4: 'a',
        q5: 'b',
        q6: 'b',
        q7: 'c',
        q8: 'c',
        q9: 'b',
        q10: 'b'
    };
    
    // Timer functionality
    let timeLeft = 15 * 60; // 15 minutes in seconds
    let timerInterval;
    
    function startTimer() {
        if (timerInterval) clearInterval(timerInterval);
        
        timerInterval = setInterval(() => {
            timeLeft--;
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            
            if (timerElement) {
                timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            }
            
            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                submitQuiz();
            }
        }, 1000);
    }
    
    // Start the timer when the page loads
    if (timerElement) {
        startTimer();
    }
    
    // Submit quiz function
    function submitQuiz() {
        clearInterval(timerInterval);
        
        let score = 0;
        const userAnswers = {};
        
        // Get user answers
        for (let i = 1; i <= 10; i++) {
            const questionName = `q${i}`;
            const selectedOption = document.querySelector(`input[name="${questionName}"]:checked`);
            if (selectedOption) {
                userAnswers[questionName] = selectedOption.value;
                if (selectedOption.value === correctAnswers[questionName]) {
                    score++;
                }
            }
        }
        
        // Calculate percentage
        const percentage = Math.round((score / 10) * 100);
        
        // Display results
        const scoreElement = document.getElementById('score');
        const percentageElement = document.getElementById('percentage');
        const resultMessage = document.getElementById('resultMessage');
        
        if (scoreElement) scoreElement.textContent = score;
        if (percentageElement) percentageElement.textContent = percentage;
        
        if (resultMessage) {
            if (percentage >= 80) {
                resultMessage.textContent = 'Excellent! You have a strong understanding of the material.';
                resultMessage.style.color = 'green';
            } else if (percentage >= 60) {
                resultMessage.textContent = 'Good job! You have a decent understanding of the material.';
                resultMessage.style.color = 'blue';
            } else {
                resultMessage.textContent = 'Keep studying! Review the material and try again.';
                resultMessage.style.color = 'orange';
            }
        }
        
        // Show results section and hide quiz
        if (quizForm) {
            quizForm.style.display = 'none';
        }
        
        const quizResults = document.getElementById('quizResults');
        if (quizResults) {
            quizResults.style.display = 'block';
            
            // Scroll to results
            quizResults.scrollIntoView({ behavior: 'smooth' });
        }
    }
    
    // Reset quiz function
    function resetQuiz() {
        // Reset all radio buttons
        const radioButtons = document.querySelectorAll('input[type="radio"]');
        radioButtons.forEach(radio => {
            radio.checked = false;
        });
        
        // Reset timer
        clearInterval(timerInterval);
        timeLeft = 15 * 60;
        
        if (timerElement) {
            const minutes = Math.floor(timeLeft / 60);
            const seconds = timeLeft % 60;
            timerElement.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        }
        
        startTimer();
        
        // Hide results and show quiz
        const quizResults = document.getElementById('quizResults');
        if (quizResults) {
            quizResults.style.display = 'none';
        }
        
        if (quizForm) {
            quizForm.style.display = 'block';
        }
    }
    
    // Event listeners
    if (submitQuizBtn) {
        submitQuizBtn.addEventListener('click', submitQuiz);
    }
    
    if (resetQuizBtn) {
        resetQuizBtn.addEventListener('click', resetQuiz);
    }
}

// Video player functionality
function initVideoPlayer() {
    const playPauseBtn = document.getElementById('playPauseBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const volumeSlider = document.getElementById('volumeSlider');
    
    if (playPauseBtn) {
        playPauseBtn.addEventListener('click', function() {
            if (playPauseBtn.textContent === 'Play') {
                playPauseBtn.textContent = 'Pause';
            } else {
                playPauseBtn.textContent = 'Play';
            }
        });
    }
    
    if (downloadBtn) {
        downloadBtn.addEventListener('click', function() {
            alert('Lecture download started. This may take a moment depending on your connection speed.');
        });
    }
    
    if (volumeSlider) {
        volumeSlider.addEventListener('input', function() {
            // In a real implementation, this would control the video volume
            console.log('Volume set to: ' + volumeSlider.value + '%');
        });
    }
}

// Download functionality for notes
function initNotesDownload() {
    const downloadPdfBtn = document.getElementById('downloadPdfBtn');
    const downloadTxtBtn = document.getElementById('downloadTxtBtn');
    
    if (downloadPdfBtn) {
        downloadPdfBtn.addEventListener('click', function() {
            alert('PDF download started. This may take a moment depending on your connection speed.');
        });
    }
    
    if (downloadTxtBtn) {
        downloadTxtBtn.addEventListener('click', function() {
            alert('Text file download started. This may take a moment depending on your connection speed.');
        });
    }
}

// Initialize notes download when on notes page
document.addEventListener('DOMContentLoaded', function() {
    if (document.body.classList.contains('notes-page')) {
        initNotesDownload();
    }
});