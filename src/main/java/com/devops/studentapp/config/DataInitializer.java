package com.devops.studentapp.config;

import com.devops.studentapp.model.Student;
import com.devops.studentapp.repository.StudentRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DataInitializer {

    @Bean
    CommandLineRunner initDatabase(StudentRepository repository) {
        return args -> {
            if (repository.count() == 0) {
                repository.save(new Student("Rahul", "Sharma", "rahul.sharma@email.com", "Computer Science", "9876543210"));
                repository.save(new Student("Priya", "Patel", "priya.patel@email.com", "Electronics", "9876543211"));
                repository.save(new Student("Amit", "Kumar", "amit.kumar@email.com", "Mechanical", "9876543212"));
                repository.save(new Student("Sneha", "Reddy", "sneha.reddy@email.com", "Computer Science", "9876543213"));
                repository.save(new Student("Vikram", "Singh", "vikram.singh@email.com", "Civil", "9876543214"));
                System.out.println(">>> Sample student data loaded successfully!");
            }
        };
    }
}

