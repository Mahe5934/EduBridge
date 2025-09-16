# Product Requirements Document (PRD)

* **Project Title:** EduBridge 
* **Project Description:** Remote Classes for Rural Colleges 
* **Prepared By:** Madhavi Anambattu 
* **Date:** 16 Sep, 2025 

---

## 1. Introduction

### 1.1 Background

Many rural colleges lack access to expert teachers and modern learning resources. While internet connectivity is improving, affordable and simple technical solutions are still needed. A lightweight backend (without heavy frameworks like Django/Flask) can help rural institutions access educational content with low infrastructure requirements.

### 1.2 Objective

The objective is to design and implement a **basic remote learning system** using a minimal Python backend (`http.server`), smart classrooms, and affordable devices. This system will allow students to:

* View live or recorded lectures.
* Access notes, quizzes, and resources.
* Connect with teachers via digital tools.

---

## 2. Proposed Solution

* **Backend:** Built with Python’s built-in `http.server`, handling basic HTTP requests and serving educational content.
* **Frontend:** HTML/CSS/JS web pages for students and teachers.
* **Smart Classrooms:** Projectors, smartboards, and internet-enabled devices for group learning.
* **Student Access:** Low-cost tablets/smartphones or community computer labs.
* **Content Library:** Central repository of video lectures, notes, and quizzes in local languages.

---

## 3. Scope

### 3.1 In Scope

* Simple backend with Python (`http.server`).
* Endpoints for lectures, notes, and quizzes (served as JSON/HTML).
* Basic web pages for student interaction.
* Offline access to recorded sessions.
* AI chatbot (optional extension for future).

### 3.2 Out of Scope

* Full-fledged LMS (Learning Management System) features.
* Complex user authentication systems.
* Advanced analytics and grading.

---

## 4. Stakeholders

* **Students:** Rural college learners.
* **Teachers:** Subject experts from urban universities.
* **Administrators:** Rural college staff managing content.
* **Support Staff:** IT team for maintaining backend and hardware.

---

## 5. Technologies & Tools

* **Backend:** Python `http.server` (minimal backend).
* **Frontend:** HTML, CSS, JavaScript.
* **Database (optional):** JSON/CSV files or SQLite for content storage.
* **AI Tools (optional):** Chatbot (Rasa/Dialogflow), Speech-to-Text API.
* **Hardware:** Smartboards, projectors, tablets, laptops.

---

## 6. Methods / Implementation Plan

1. **Setup Basic Backend:** Serve HTML/JSON using Python `http.server`.
2. **Frontend Pages:** Create course pages with lecture lists.
3. **Content Upload:** Add lecture videos, notes, and quizzes in local languages.
4. **Smart Classroom Installation:** Projectors, screens, internet setup.
5. **Pilot Run:** Test in 1–2 rural colleges.
6. **Feedback & Iteration:** Collect feedback from students and improve system.

---

## 7. Functional Requirements

* **Course Access:** Students can view available courses and lectures.
* **Notes & Quizzes:** Download notes and attempt quizzes.
* **Recorded Content:** Access stored video lectures.
* **Basic Navigation:** Homepage, About page, Course page.
* **Multi-language Support:** Content available in local languages.

---

## 8. Non-Functional Requirements

* **Lightweight:** Runs without heavy frameworks.
* **Low Bandwidth Friendly:** Optimized for rural internet speeds.
* **Scalable:** Content can be expanded easily.
* **Secure (Basic):** Prevent unauthorized file changes on the server.
* **Usability:** Simple, clean design for first-time digital learners.

---

## 9. Success Metrics

* Number of students accessing lectures.
* Number of courses/content uploaded.
* Usage frequency (daily/weekly access).
* Student feedback on content accessibility.
* Teacher participation rate.

---

## 10. Risks & Mitigation

* **Limited Features:** Minimal backend may lack advanced functions → Future upgrade to FastAPI/Django if needed.
* **Internet Issues:** Provide offline downloadable lectures.
* **Device Shortage:** Use community computer labs.
* **Training Gaps:** Conduct orientation for teachers and students.

---

## 11. Timeline (Sample – 3 Months Project)

* **Month 1:** Develop basic backend + frontend pages.
* **Month 2:** Add content (lectures, notes, quizzes) + smart classroom setup.
* **Month 3:** Pilot test in rural colleges + feedback collection.

---

## 12. Budget (Indicative)

* **Backend Development:** Minimal (student project).
* **Hardware (per college):** ₹2–3 lakhs (projector, smartboard, internet).
* **Devices for Students:** ₹6,000–₹10,000 per tablet.
* **Maintenance:** ₹1–2 lakhs annually.

---