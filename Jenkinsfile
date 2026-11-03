// ============================================
// JENKINSFILE - CI/CD PIPELINE
// Student Management Application
// ============================================
// This pipeline automates: Build → Test → Package → Docker → Deploy → Verify
// ============================================

pipeline {
    agent any

    environment {
        APP_NAME        = 'student-management-app'
        APP_VERSION     = '1.0.0'
        DOCKER_IMAGE    = "${env.DOCKER_REGISTRY ?: 'local'}/${APP_NAME}"
        DOCKER_TAG      = "${APP_VERSION}-${BUILD_NUMBER}"
        DEPLOY_PORT     = '8080'
    }

    tools {
        maven 'Maven-3.9'   // Configure in Jenkins: Manage Jenkins → Tools
        jdk   'JDK-17'      // Configure in Jenkins: Manage Jenkins → Tools
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    stages {
        // ==============================
        // STAGE 1: CHECKOUT
        // ==============================
        stage('Checkout') {
            steps {
                echo '📥 Pulling latest source code from GitHub...'
                checkout scm
                echo "✅ Checkout complete - Branch: ${env.GIT_BRANCH}"
            }
        }

        // ==============================
        // STAGE 2: BUILD
        // ==============================
        stage('Build') {
            steps {
                echo '🔨 Building application with Maven...'
                bat 'mvn clean compile -B'  // Use 'sh' for Linux
                echo '✅ Build completed successfully!'
            }
        }

        // ==============================
        // STAGE 3: UNIT TESTING
        // ==============================
        stage('Unit Testing') {
            steps {
                echo '🧪 Running JUnit test cases...'
                bat 'mvn test -B'  // Use 'sh' for Linux
            }
            post {
                always {
                    junit allowEmptyResults: true,
                         testResults: 'target/surefire-reports/*.xml'
                }
                success {
                    echo '✅ All tests passed!'
                }
                failure {
                    echo '❌ Some tests failed! Check the test report.'
                }
            }
        }

        // ==============================
        // STAGE 4: PACKAGE
        // ==============================
        stage('Package') {
            steps {
                echo '📦 Creating JAR artifact...'
                bat 'mvn package -DskipTests -B'  // Use 'sh' for Linux
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
                echo '✅ JAR file created successfully!'
            }
        }

        // ==============================
        // STAGE 5: DOCKER BUILD
        // ==============================
        stage('Docker Build') {
            steps {
                echo '🐳 Building Docker image...'
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} -t ${DOCKER_IMAGE}:latest ."
                }
                echo "✅ Docker image built: ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }

        // ==============================
        // STAGE 6: DOCKER PUSH (Optional)
        // ==============================
        stage('Docker Push') {
            when {
                environment name: 'DOCKER_PUSH', value: 'true'
            }
            steps {
                echo '📤 Pushing Docker image to registry...'
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'docker-hub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        bat "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                        bat "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                        bat "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
                echo '✅ Docker image pushed successfully!'
            }
        }

        // ==============================
        // STAGE 7: DEPLOYMENT
        // ==============================
        stage('Deploy') {
            steps {
                echo '🚀 Deploying application...'
                script {
                    // Stop existing container if running
                    bat "docker stop ${APP_NAME} || exit 0"
                    bat "docker rm ${APP_NAME} || exit 0"

                    // Deploy new container
                    bat """
                        docker run -d \
                            --name ${APP_NAME} \
                            -p ${DEPLOY_PORT}:8080 \
                            -e SPRING_PROFILES_ACTIVE=dev \
                            --restart unless-stopped \
                            ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
                echo "✅ Application deployed on port ${DEPLOY_PORT}"
            }
        }

        // ==============================
        // STAGE 8: DEPLOYMENT VERIFICATION
        // ==============================
        stage('Verify Deployment') {
            steps {
                echo '🔍 Verifying deployment...'
                script {
                    // Wait for app to start
                    sleep(time: 20, unit: 'SECONDS')

                    // Health check
                    bat """
                        curl -s -o NUL -w "HTTP_STATUS:%%{http_code}" http://localhost:${DEPLOY_PORT}/actuator/health
                    """
                }
                echo '✅ Deployment verified - Application is healthy!'
            }
        }
    }

    // ==============================
    // POST ACTIONS
    // ==============================
    post {
        success {
            echo """
            ╔══════════════════════════════════════════════╗
            ║  ✅ PIPELINE COMPLETED SUCCESSFULLY!         ║
            ║  App: http://localhost:${DEPLOY_PORT}              ║
            ║  Build: #${BUILD_NUMBER}                          ║
            ║  Image: ${DOCKER_IMAGE}:${DOCKER_TAG}       ║
            ╚══════════════════════════════════════════════╝
            """
        }
        failure {
            echo """
            ╔══════════════════════════════════════════════╗
            ║  ❌ PIPELINE FAILED!                         ║
            ║  Build: #${BUILD_NUMBER}                          ║
            ║  Check the logs for error details.           ║
            ╚══════════════════════════════════════════════╝
            """
        }
        always {
            echo "Pipeline finished at: ${new Date()}"
            cleanWs()
        }
    }
}

