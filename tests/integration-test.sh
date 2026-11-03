#!/bin/bash
# ============================================
# Integration Test Script (Linux/Mac)
# Tests all API endpoints after deployment
# ============================================

echo "============================================"
echo "  Running Integration Tests"
echo "  Target: http://localhost:8080"
echo "============================================"

BASE_URL="http://localhost:8080"
PASS=0
FAIL=0

run_test() {
    local name="$1"
    local method="$2"
    local url="$3"
    local data="$4"

    echo ""
    echo "[TEST] $name..."

    if [ -n "$data" ]; then
        STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X "$method" "$url" \
            -H "Content-Type: application/json" -d "$data")
    else
        STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X "$method" "$url")
    fi

    if [ "$STATUS" -ge 200 ] && [ "$STATUS" -lt 400 ]; then
        echo "  ✅ PASSED (HTTP $STATUS)"
        PASS=$((PASS + 1))
    else
        echo "  ❌ FAILED (HTTP $STATUS)"
        FAIL=$((FAIL + 1))
    fi
}

run_test "Health Check" "GET" "$BASE_URL/actuator/health"
run_test "Get All Students" "GET" "$BASE_URL/api/students"
run_test "Create Student" "POST" "$BASE_URL/api/students" \
    '{"firstName":"Test","lastName":"User","email":"test@integration.com","department":"QA","phone":"0000000000"}'
run_test "Get Student Stats" "GET" "$BASE_URL/api/students/stats"
run_test "Frontend Page" "GET" "$BASE_URL/index.html"

echo ""
echo "============================================"
echo "  Results: $PASS Passed, $FAIL Failed"
echo "============================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1

