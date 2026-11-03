package com.devops.studentapp.repository;

import com.devops.studentapp.model.Student;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@DataJpaTest
class StudentRepositoryTest {

    @Autowired
    private StudentRepository studentRepository;

    @Test
    void saveStudent_ShouldPersistStudent() {
        Student student = new Student("Test", "User", "test@email.com", "CS", "1234567890");
        Student saved = studentRepository.save(student);

        assertNotNull(saved.getId());
        assertEquals("Test", saved.getFirstName());
    }

    @Test
    void findByEmail_WhenExists_ShouldReturnStudent() {
        Student student = new Student("Alex", "Smith", "unique@email.com", "CS", "1234567890");
        studentRepository.save(student);

        Optional<Student> found = studentRepository.findByEmail("unique@email.com");

        assertTrue(found.isPresent());
        assertEquals("Alex", found.get().getFirstName());
    }

    @Test
    void findByDepartment_ShouldReturnMatchingStudents() {
        studentRepository.save(new Student("Alice", "Brown", "a@email.com", "Physics", "111"));
        studentRepository.save(new Student("Charlie", "Davis", "c@email.com", "Physics", "222"));
        studentRepository.save(new Student("Emma", "Frank", "e@email.com", "Chemistry", "333"));

        List<Student> physics = studentRepository.findByDepartment("Physics");

        assertEquals(2, physics.size());
    }

    @Test
    void existsByEmail_WhenExists_ShouldReturnTrue() {
        studentRepository.save(new Student("Xavier", "Young", "exists@email.com", "Math", "444"));

        assertTrue(studentRepository.existsByEmail("exists@email.com"));
        assertFalse(studentRepository.existsByEmail("notexists@email.com"));
    }
}
