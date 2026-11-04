@echo off
title Jenkins CI/CD Automation Server (Port 8081)
echo ===================================================
echo   Starting Jenkins CI/CD Server on Port 8081...
echo   URL: http://localhost:8081
echo ===================================================
"C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\java.exe" -jar C:\jenkins\jenkins.war --httpPort=8081
pause

