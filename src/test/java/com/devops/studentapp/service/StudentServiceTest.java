package com.devops.studentapp.service;

import com.devops.studentapp.model.Student;
import com.devops.studentapp.repository.StudentRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class StudentServiceTest {

    @Mock
    private StudentRepository studentRepository;

    @InjectMocks
    private StudentServiceImpl studentService;

    private Student testStudent;

    @BeforeEach
    void setUp() {
        testStudent = new Student("Priya", "Patel", "priya@email.com", "Electronics", "9876543211");
        testStudent.setId(1L);
    }

    @Test
    void getAllStudents_ShouldReturnAllStudents() {
        List<Student> students = Arrays.asList(testStudent);
        when(studentRepository.findAll()).thenReturn(students);

        List<Student> result = studentService.getAllStudents();

        assertEquals(1, result.size());
        assertEquals("Priya", result.get(0).getFirstName());
        verify(studentRepository, times(1)).findAll();
    }

    @Test
    void getStudentById_WhenExists_ShouldReturnStudent() {
        when(studentRepository.findById(1L)).thenReturn(Optional.of(testStudent));

        Optional<Student> result = studentService.getStudentById(1L);

        assertTrue(result.isPresent());
        assertEquals("Priya", result.get().getFirstName());
    }

    @Test
    void createStudent_WithNewEmail_ShouldSaveStudent() {
        when(studentRepository.existsByEmail("priya@email.com")).thenReturn(false);
        when(studentRepository.save(any(Student.class))).thenReturn(testStudent);

        Student result = studentService.createStudent(testStudent);

        assertNotNull(result);
        assertEquals("Priya", result.getFirstName());
        verify(studentRepository).save(testStudent);
    }

    @Test
    void createStudent_WithDuplicateEmail_ShouldThrowException() {
        when(studentRepository.existsByEmail("priya@email.com")).thenReturn(true);

        assertThrows(RuntimeException.class, () -> studentService.createStudent(testStudent));
        verify(studentRepository, never()).save(any());
    }

    @Test
    void deleteStudent_WhenExists_ShouldDeleteStudent() {
        when(studentRepository.findById(1L)).thenReturn(Optional.of(testStudent));
        doNothing().when(studentRepository).delete(testStudent);

        assertDoesNotThrow(() -> studentService.deleteStudent(1L));
        verify(studentRepository).delete(testStudent);
    }

    @Test
    void deleteStudent_WhenNotExists_ShouldThrowException() {
        when(studentRepository.findById(99L)).thenReturn(Optional.empty());

        assertThrows(RuntimeException.class, () -> studentService.deleteStudent(99L));
    }

    @Test
    void getStudentCount_ShouldReturnCount() {
        when(studentRepository.count()).thenReturn(5L);

        long count = studentService.getStudentCount();

        assertEquals(5L, count);
    }
}

