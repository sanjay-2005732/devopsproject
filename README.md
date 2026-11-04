# 🚀 Automated CI/CD Pipeline
## Student Management Application

[![Build Status](https://img.shields.io/badge/Jenkins%20CI-Passing-brightgreen)](http://localhost:8081/job/student-pipeline/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Passing-brightgreen)](https://github.com/sanjay-2005732/devopsproject/actions)
[![Java](https://img.shields.io/badge/Java-17-orange)](/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.2.0-green)](/)
[![Maven](https://img.shields.io/badge/Maven-3.9.6-red)](/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](/)
[![Jenkins](https://img.shields.io/badge/Jenkins-Pipeline-red)](http://localhost:8081)
[![License](https://img.shields.io/badge/license-MIT-blue)](/)

A complete **Student Management Web Application** with an **Automated CI/CD Pipeline** using **Jenkins, GitHub, Maven, Docker, and AWS**.

---

## 📋 Table of Contents

- [Project Introduction](#-project-introduction)
- [Objectives](#-objectives)
- [Technologies Used](#-technologies-used)
- [System Architecture](#-system-architecture)
- [CI/CD Workflow](#-cicd-workflow)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [Jenkins Configuration](#-jenkins-configuration)
- [GitHub Webhook Setup](#-github-webhook-setup)
- [Docker Configuration](#-docker-configuration)
- [AWS Deployment](#-aws-deployment)
- [API Documentation](#-api-documentation)
- [Screenshots](#-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Expected Output](#-expected-output)

---

## 📖 Project Introduction

This project demonstrates a complete **DevOps CI/CD pipeline** that automatically **builds, tests, packages, and deploys** a web application whenever a developer pushes code to GitHub. The application is a **Student Management System** built with **Java Spring Boot** that supports full CRUD (Create, Read, Update, Delete) operations.

---

## 🎯 Objectives

1. Build a functional **Student Management Web Application**
2. Implement **automated CI/CD pipeline** using Jenkins
3. Use **Maven** for build automation and dependency management
4. Run **JUnit automated tests** on every build
5. **Containerize** the application using Docker
6. **Deploy** automatically to local Docker or AWS EC2
7. Provide a **monitoring dashboard** for pipeline status

---

## 🛠 Technologies Used

| Technology | Purpose | Version |
|---|---|---|
| **Java** | Backend Programming Language | 17 |
| **Spring Boot** | Web Framework | 3.2.0 |
| **Maven** | Build Tool & Dependency Management | 3.9+ |
| **H2 Database** | In-Memory Database (Development) | 2.x |
| **MySQL** | Relational Database (Production) | 8.0 |
| **JUnit 5** | Unit Testing Framework | 5.x |
| **Git & GitHub** | Version Control | Latest |
| **Jenkins** | CI/CD Automation Server | LTS |
| **Docker** | Containerization | Latest |
| **Docker Compose** | Multi-Container Orchestration | 3.8 |
| **AWS EC2** | Cloud Deployment (Optional) | - |
| **HTML/CSS/JS** | Frontend User Interface | ES6+ |

---

## 🏗 System Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Developer  │────▶│    GitHub     │────▶│   Jenkins    │
│   (Code)     │push │ (Repository) │hook │  (CI/CD)     │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                     ┌────────────────────────────┼────────────────┐
                     │                            │                │
                     ▼                            ▼                ▼
              ┌──────────────┐          ┌──────────────┐  ┌──────────────┐
              │  Maven Build │          │   JUnit      │  │   Docker     │
              │  & Compile   │          │   Tests      │  │   Build      │
              └──────────────┘          └──────────────┘  └──────┬───────┘
                                                                  │
                                                                  ▼
                                                         ┌──────────────┐
                                                         │   Deploy     │
                                                         │  (Docker /   │
                                                         │   AWS EC2)   │
                                                         └──────────────┘
```

---

## 🔄 CI/CD Workflow

```
Step 1: Developer writes code
    │
    ▼
Step 2: Push to GitHub
    │
    ▼
Step 3: GitHub webhook triggers Jenkins ──────────────────────┐
    │                                                          │
    ▼                                                          │
Step 4: Jenkins pulls latest code                              │
    │                                                          │
    ▼                                                          │
Step 5: Maven builds the application                           │
    │                                                          │
    ▼                                                     On Failure:
Step 6: JUnit runs automated tests ──────────────────▶  Stop & Report
    │                                                     Error
    ▼
Step 7: Create application JAR
    │
    ▼
Step 8: Docker builds container image
    │
    ▼
Step 9: Deploy to Docker / AWS EC2
    │
    ▼
Step 10: Verify deployment (health check)
```

---

## 📁 Project Structure

```
devopsproject/
├── frontend/                        # Frontend reference files
│   └── README.md
├── backend/                         # Backend documentation
│   └── README.md
├── src/
│   ├── main/
│   │   ├── java/com/devops/studentapp/
│   │   │   ├── StudentApplication.java          # Main entry point
│   │   │   ├── config/
│   │   │   │   └── DataInitializer.java         # Sample data loader
│   │   │   ├── controller/
│   │   │   │   └── StudentController.java       # REST API controller
│   │   │   ├── exception/
│   │   │   │   └── GlobalExceptionHandler.java  # Error handling
│   │   │   ├── model/
│   │   │   │   └── Student.java                 # JPA Entity
│   │   │   ├── repository/
│   │   │   │   └── StudentRepository.java       # Data access
│   │   │   └── service/
│   │   │       ├── StudentService.java          # Service interface
│   │   │       └── StudentServiceImpl.java      # Service implementation
│   │   └── resources/
│   │       ├── application.properties           # App config (H2)
│   │       ├── application-docker.properties    # Docker config (MySQL)
│   │       └── static/
│   │           ├── index.html                   # Student Management UI
│   │           ├── dashboard.html               # CI/CD Dashboard
│   │           ├── css/style.css                # Styles
│   │           └── js/app.js                    # Frontend JavaScript
│   └── test/
│       └── java/com/devops/studentapp/
│           ├── StudentApplicationTests.java     # Context test
│           ├── controller/
│           │   └── StudentControllerTest.java   # Controller tests
│           ├── repository/
│           │   └── StudentRepositoryTest.java   # Repository tests
│           └── service/
│               └── StudentServiceTest.java      # Service tests
├── tests/
│   ├── integration-test.bat                     # Windows integration tests
│   └── integration-test.sh                      # Linux integration tests
├── pom.xml                                      # Maven configuration
├── Dockerfile                                   # Docker image definition
├── docker-compose.yml                           # Docker Compose config
├── Jenkinsfile                                  # Jenkins pipeline
├── .gitignore                                   # Git ignore rules
├── .env.example                                 # Environment variables template
└── README.md                                    # This file
```

---

## 🚀 Installation & Setup

### Prerequisites

| Tool | Required | Install Command / Link |
|---|---|---|
| **Java JDK 17+** | ✅ | [Download](https://adoptium.net/) |
| **Maven 3.9+** | ✅ | [Download](https://maven.apache.org/download.cgi) |
| **Git** | ✅ | [Download](https://git-scm.com/downloads) |
| **Docker** | Optional | [Download](https://www.docker.com/products/docker-desktop/) |
| **Jenkins** | Optional | [Download](https://www.jenkins.io/download/) |

### Step 1: Clone the Repository

```bash
# Clone the project
git clone https://github.com/your-username/devopsproject.git
cd devopsproject
```

### Step 2: Verify Prerequisites

```bash
# Check Java
java -version

# Check Maven
mvn -version

# Check Git
git --version

# Check Docker (optional)
docker --version
```

---

## ▶️ Running the Application

### Option 1: Run with Maven (Simplest - Recommended for beginners)

**Windows:**
```cmd
cd c:\devopsproject
mvn clean install
mvn spring-boot:run
```

**Linux/Mac:**
```bash
cd devopsproject
mvn clean install
mvn spring-boot:run
```

Access the application:
- 🌐 **Application**: http://localhost:8080
- 📊 **Dashboard**: http://localhost:8080/dashboard.html
- 💾 **H2 Console**: http://localhost:8080/h2-console
- ❤️ **Health Check**: http://localhost:8080/actuator/health

### Option 2: Run with Java JAR

```bash
# Build the JAR
mvn clean package -DskipTests

# Run the JAR
java -jar target/student-management-app-1.0.0.jar
```

### Option 3: Run with Docker

```bash
# Build and run with Docker Compose (H2 database)
docker-compose up --build

# OR build and run manually
docker build -t student-management-app .
docker run -p 8080:8080 student-management-app
```

### Option 4: Run with Docker + MySQL

```bash
# Start with MySQL database
docker-compose --profile mysql up --build
```

---

## ⚙️ Jenkins Configuration

### Step 1: Install Jenkins

**Windows:**
1. Download Jenkins from https://www.jenkins.io/download/
2. Run the installer
3. Access Jenkins at http://localhost:8081

**Using Docker:**
```bash
docker-compose --profile cicd up jenkins
```

### Step 2: Install Required Jenkins Plugins

Go to **Manage Jenkins → Plugins → Available Plugins** and install:
- ✅ Git Plugin
- ✅ Maven Integration Plugin
- ✅ Pipeline Plugin
- ✅ Docker Pipeline Plugin
- ✅ GitHub Integration Plugin

### Step 3: Configure Tools

Go to **Manage Jenkins → Tools**:

1. **JDK Installation:**
   - Name: `JDK-17`
   - Install automatically → AdoptOpenJDK 17

2. **Maven Installation:**
   - Name: `Maven-3.9`
   - Install automatically → Version 3.9.x

### Step 4: Create Pipeline Job

1. Click **New Item**
2. Name: `student-management-pipeline`
3. Select **Pipeline**
4. Under **Pipeline**:
   - Definition: `Pipeline script from SCM`
   - SCM: `Git`
   - Repository URL: `https://github.com/your-username/devopsproject.git`
   - Branch: `*/main`
   - Script Path: `Jenkinsfile`
5. Click **Save**

### Step 5: Run the Pipeline

Click **Build Now** to trigger the pipeline manually.

---

## 🔗 GitHub Webhook Setup

### Step 1: Configure Jenkins

1. Go to **Manage Jenkins → Configure System**
2. Under **GitHub**:
   - Add GitHub Server
   - Credentials: Add your GitHub Personal Access Token

### Step 2: Configure GitHub Repository

1. Go to your GitHub repo → **Settings → Webhooks**
2. Click **Add webhook**
3. **Payload URL:** `http://your-jenkins-url:8081/github-webhook/`
4. **Content type:** `application/json`
5. **Events:** Select `Just the push event`
6. Click **Add webhook**

### Step 3: Configure Jenkins Job

1. Open your pipeline job → **Configure**
2. Under **Build Triggers**:
   - ✅ Check `GitHub hook trigger for GITScm polling`
3. Click **Save**

Now every `git push` will automatically trigger the pipeline!

---

## 🐳 Docker Configuration

### Dockerfile Explanation

The project uses a **multi-stage Docker build**:
- **Stage 1 (Builder):** Uses Maven to compile and package the application
- **Stage 2 (Runtime):** Uses lightweight JRE Alpine image for production

### Docker Commands Reference

```bash
# Build image
docker build -t student-management-app .

# Run container
docker run -d -p 8080:8080 --name student-app student-management-app

# View logs
docker logs -f student-app

# Stop container
docker stop student-app

# Remove container
docker rm student-app

# Docker Compose
docker-compose up --build        # H2 database
docker-compose --profile mysql up --build  # With MySQL
docker-compose down              # Stop all
```

---

## ☁️ AWS Deployment

### Step 1: Launch EC2 Instance

1. Go to AWS Console → EC2 → Launch Instance
2. Choose **Amazon Linux 2** or **Ubuntu 22.04**
3. Instance type: **t2.micro** (free tier)
4. Configure Security Group:
   - SSH: Port 22
   - HTTP: Port 80
   - Custom TCP: Port 8080
5. Create and download key pair

### Step 2: Install Docker on EC2

```bash
# SSH into EC2
ssh -i your-key.pem ec2-user@your-ec2-public-ip

# Install Docker (Amazon Linux)
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -aG docker ec2-user

# Install Docker (Ubuntu)
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo usermod -aG docker ubuntu
```

### Step 3: Deploy Application

```bash
# Pull and run (if using Docker Hub)
docker pull your-dockerhub-username/student-management-app:latest
docker run -d -p 8080:8080 --name student-app \
    your-dockerhub-username/student-management-app:latest

# OR build on EC2
git clone https://github.com/your-username/devopsproject.git
cd devopsproject
docker build -t student-management-app .
docker run -d -p 8080:8080 --name student-app student-management-app
```

### Step 4: Access Application

Open browser: `http://your-ec2-public-ip:8080`

---

## 📡 API Documentation

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/students` | Get all students |
| `GET` | `/api/students/{id}` | Get student by ID |
| `POST` | `/api/students` | Create new student |
| `PUT` | `/api/students/{id}` | Update student |
| `DELETE` | `/api/students/{id}` | Delete student |
| `GET` | `/api/students/search?keyword=xxx` | Search students |
| `GET` | `/api/students/department/{dept}` | Filter by department |
| `GET` | `/api/students/stats` | Get statistics |
| `GET` | `/actuator/health` | Health check |

### Example API Requests

```bash
# Create a student
curl -X POST http://localhost:8080/api/students \
  -H "Content-Type: application/json" \
  -d '{"firstName":"John","lastName":"Doe","email":"john@email.com","department":"Computer Science","phone":"1234567890"}'

# Get all students
curl http://localhost:8080/api/students

# Update a student
curl -X PUT http://localhost:8080/api/students/1 \
  -H "Content-Type: application/json" \
  -d '{"firstName":"John","lastName":"Updated","email":"john@email.com","department":"IT","phone":"0987654321"}'

# Delete a student
curl -X DELETE http://localhost:8080/api/students/1
```

---

## 📸 Screenshots

### Student Management Application
> Access at: http://localhost:8080
- Home page with student list
- Add/Edit student modal form
- Search and filter functionality

### CI/CD Dashboard
> Access at: http://localhost:8080/dashboard.html
- Pipeline status indicators (green/red/yellow)
- Build history with pass/fail status
- Pipeline execution logs
- Docker image and deployment status

### Jenkins Pipeline
> Access at: http://localhost:8081
- Blue Ocean pipeline visualization
- Stage-by-stage execution view
- Test results summary

---

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|---|---|
| `Port 8080 already in use` | Change port in `application.properties` or use `--server.port=8081` |
| `Maven build fails` | Run `mvn clean install -U` to force update dependencies |
| `Java version mismatch` | Ensure JDK 17+ is installed: `java -version` |
| `Docker permission denied` | Run `sudo usermod -aG docker $USER` and re-login |
| `Jenkins can't find Maven` | Configure Maven in Jenkins: Manage Jenkins → Tools |
| `H2 Console not accessible` | Ensure `spring.h2.console.enabled=true` in properties |
| `Tests fail` | Run `mvn test -X` for verbose output |
| `Docker build fails` | Ensure Docker daemon is running: `docker info` |

### Useful Debug Commands

```bash
# Check application logs
mvn spring-boot:run | tee app.log

# Check Docker container logs
docker logs -f student-management-app

# Test API connectivity
curl -v http://localhost:8080/actuator/health

# Check running containers
docker ps -a

# Check Maven dependencies
mvn dependency:tree
```

---

## ✅ Expected Output

### Application Running
```
============================================
  Student Management App is Running!
  URL: http://localhost:8080
  H2 Console: http://localhost:8080/h2-console
  Health: http://localhost:8080/actuator/health
============================================
>>> Sample student data loaded successfully!
```

### Health Check Response
```json
{
  "status": "UP",
  "components": {
    "db": { "status": "UP" },
    "diskSpace": { "status": "UP" }
  }
}
```

### API Response (Get All Students)
```json
{
  "success": true,
  "count": 5,
  "data": [
    {
      "id": 1,
      "firstName": "Rahul",
      "lastName": "Sharma",
      "email": "rahul.sharma@email.com",
      "department": "Computer Science",
      "phone": "9876543210"
    }
  ]
}
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👥 Contributors

- **DevOps Team** - Project Development & CI/CD Pipeline

---

> **⭐ If this project helped you, please give it a star on GitHub!**

