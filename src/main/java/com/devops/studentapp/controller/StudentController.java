package com.devops.studentapp.controller;

import com.devops.studentapp.model.Student;
import com.devops.studentapp.service.StudentService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/students")
@CrossOrigin(origins = "*")
public class StudentController {

    private final StudentService studentService;

    @Autowired
    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }

    // GET /api/students - Get all students
    @GetMapping
    public ResponseEntity<Map<String, Object>> getAllStudents() {
        List<Student> students = studentService.getAllStudents();
        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("data", students);
        response.put("count", students.size());
        return ResponseEntity.ok(response);
    }

    // GET /api/students/{id} - Get student by ID
    @GetMapping("/{id}")
    public ResponseEntity<Map<String, Object>> getStudentById(@PathVariable Long id) {
        Map<String, Object> response = new HashMap<>();
        return studentService.getStudentById(id)
                .map(student -> {
                    response.put("success", true);
                    response.put("data", student);
                    return ResponseEntity.ok(response);
                })
                .orElseGet(() -> {
                    response.put("success", false);
                    response.put("error", "Student not found with id: " + id);
                    return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
                });
    }

    // POST /api/students - Create a new student
    @PostMapping
    public ResponseEntity<Map<String, Object>> createStudent(@Valid @RequestBody Student student) {
        Map<String, Object> response = new HashMap<>();
        try {
            Student created = studentService.createStudent(student);
            response.put("success", true);
            response.put("data", created);
            response.put("message", "Student created successfully");
            return ResponseEntity.status(HttpStatus.CREATED).body(response);
        } catch (RuntimeException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(response);
        }
    }

    // PUT /api/students/{id} - Update a student
    @PutMapping("/{id}")
    public ResponseEntity<Map<String, Object>> updateStudent(
            @PathVariable Long id, @Valid @RequestBody Student student) {
        Map<String, Object> response = new HashMap<>();
        try {
            Student updated = studentService.updateStudent(id, student);
            response.put("success", true);
            response.put("data", updated);
            response.put("message", "Student updated successfully");
            return ResponseEntity.ok(response);
        } catch (RuntimeException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
        }
    }

    // DELETE /api/students/{id} - Delete a student
    @DeleteMapping("/{id}")
    public ResponseEntity<Map<String, Object>> deleteStudent(@PathVariable Long id) {
        Map<String, Object> response = new HashMap<>();
        try {
            studentService.deleteStudent(id);
            response.put("success", true);
            response.put("message", "Student deleted successfully");
            return ResponseEntity.ok(response);
        } catch (RuntimeException e) {
            response.put("success", false);
            response.put("error", e.getMessage());
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
        }
    }

    // GET /api/students/search?keyword=xxx - Search students
    @GetMapping("/search")
    public ResponseEntity<Map<String, Object>> searchStudents(@RequestParam String keyword) {
        List<Student> students = studentService.searchStudents(keyword);
        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("data", students);
        response.put("count", students.size());
        return ResponseEntity.ok(response);
    }

    // GET /api/students/department/{dept} - Get by department
    @GetMapping("/department/{department}")
    public ResponseEntity<Map<String, Object>> getByDepartment(@PathVariable String department) {
        List<Student> students = studentService.getStudentsByDepartment(department);
        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("data", students);
        response.put("count", students.size());
        return ResponseEntity.ok(response);
    }

    // GET /api/students/stats - Get statistics
    @GetMapping("/stats")
    public ResponseEntity<Map<String, Object>> getStats() {
        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("totalStudents", studentService.getStudentCount());
        response.put("departments", studentService.getAllDepartments());
        return ResponseEntity.ok(response);
    }
}

