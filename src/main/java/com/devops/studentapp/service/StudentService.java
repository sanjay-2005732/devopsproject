package com.devops.studentapp.service;

import com.devops.studentapp.model.Student;
import java.util.List;
import java.util.Optional;

public interface StudentService {

    List<Student> getAllStudents();

    Optional<Student> getStudentById(Long id);

    Student createStudent(Student student);

    Student updateStudent(Long id, Student student);

    void deleteStudent(Long id);

    List<Student> searchStudents(String keyword);

    List<Student> getStudentsByDepartment(String department);

    List<String> getAllDepartments();

    long getStudentCount();
}

