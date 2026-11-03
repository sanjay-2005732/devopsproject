@echo off
REM ============================================
REM Integration Test Script (Windows)
REM Tests all API endpoints after deployment
REM ============================================

echo ============================================
echo   Running Integration Tests
echo   Target: http://localhost:8080
echo ============================================

set BASE_URL=http://localhost:8080
set PASS=0
set FAIL=0

echo.
echo [TEST 1] Health Check...
curl -s -o NUL -w "HTTP %%{http_code}" %BASE_URL%/actuator/health
if %ERRORLEVEL% EQU 0 (
    echo  - PASSED
    set /a PASS+=1
) else (
    echo  - FAILED
    set /a FAIL+=1
)

echo.
echo [TEST 2] Get All Students...
curl -s -o NUL -w "HTTP %%{http_code}" %BASE_URL%/api/students
if %ERRORLEVEL% EQU 0 (
    echo  - PASSED
    set /a PASS+=1
) else (
    echo  - FAILED
    set /a FAIL+=1
)

echo.
echo [TEST 3] Create Student...
curl -s -o NUL -w "HTTP %%{http_code}" -X POST %BASE_URL%/api/students -H "Content-Type: application/json" -d "{\"firstName\":\"Test\",\"lastName\":\"User\",\"email\":\"test@integration.com\",\"department\":\"QA\",\"phone\":\"0000000000\"}"
if %ERRORLEVEL% EQU 0 (
    echo  - PASSED
    set /a PASS+=1
) else (
    echo  - FAILED
    set /a FAIL+=1
)

echo.
echo [TEST 4] Get Student Stats...
curl -s -o NUL -w "HTTP %%{http_code}" %BASE_URL%/api/students/stats
if %ERRORLEVEL% EQU 0 (
    echo  - PASSED
    set /a PASS+=1
) else (
    echo  - FAILED
    set /a FAIL+=1
)

echo.
echo [TEST 5] Frontend Page...
curl -s -o NUL -w "HTTP %%{http_code}" %BASE_URL%/index.html
if %ERRORLEVEL% EQU 0 (
    echo  - PASSED
    set /a PASS+=1
) else (
    echo  - FAILED
    set /a FAIL+=1
)

echo.
echo ============================================
echo   Results: %PASS% Passed, %FAIL% Failed
echo ============================================

