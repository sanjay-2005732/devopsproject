@echo off
set "JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot"
set "PATH=%JAVA_HOME%\bin;%~dp0maven\apache-maven-3.9.6\bin;%PATH%"
"%~dp0maven\apache-maven-3.9.6\bin\mvn.cmd" %*

