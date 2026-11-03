This directory contains the Java Spring Boot backend source code.

The source code follows the standard Maven directory structure:
  src/main/java/com/devops/studentapp/

Package Structure:
├── StudentApplication.java          → Main application entry point
├── config/
│   └── DataInitializer.java         → Sample data loader
├── controller/
│   └── StudentController.java       → REST API endpoints
├── exception/
│   └── GlobalExceptionHandler.java  → Error handling
├── model/
│   └── Student.java                 → JPA Entity
├── repository/
│   └── StudentRepository.java       → Data access layer
└── service/
    ├── StudentService.java          → Service interface
    └── StudentServiceImpl.java      → Service implementation

API Endpoints:
  GET    /api/students          → List all students
  GET    /api/students/{id}     → Get student by ID
  POST   /api/students          → Create new student
  PUT    /api/students/{id}     → Update student
  DELETE /api/students/{id}     → Delete student
  GET    /api/students/search   → Search students
  GET    /api/students/stats    → Get statistics

