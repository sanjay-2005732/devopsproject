// ============================================
// STUDENT MANAGEMENT APP - Frontend JavaScript
// ============================================

const API_BASE = '/api/students';
let isEditing = false;

// ---- Initialize ----
document.addEventListener('DOMContentLoaded', () => {
    loadStudents();
    loadStats();
});

// ---- Load All Students ----
async function loadStudents() {
    try {
        const response = await fetch(API_BASE);
        const result = await response.json();
        if (result.success) {
            renderStudents(result.data);
        }
    } catch (error) {
        showAlert('Failed to load students. Is the server running?', 'danger');
        document.getElementById('studentsTableBody').innerHTML =
            '<tr><td colspan="7" class="no-data"><i class="fas fa-exclamation-triangle"></i> Could not connect to server</td></tr>';
    }
}

// ---- Load Statistics ----
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        const result = await response.json();
        if (result.success) {
            document.getElementById('totalStudents').textContent = result.totalStudents;
            document.getElementById('totalDepartments').textContent =
                result.departments ? result.departments.length : 0;
            document.getElementById('appStatus').innerHTML =
                '<span style="color:#10b981">● Online</span>';
        }
    } catch {
        document.getElementById('appStatus').innerHTML =
            '<span style="color:#ef4444">● Offline</span>';
    }
}

// ---- Render Students Table ----
function renderStudents(students) {
    const tbody = document.getElementById('studentsTableBody');
    if (!students || students.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" class="no-data"><i class="fas fa-inbox"></i> No students found. Click "Add Student" to get started.</td></tr>';
        return;
    }
    tbody.innerHTML = students.map(s => `
        <tr>
            <td><strong>#${s.id}</strong></td>
            <td>${escapeHtml(s.firstName)}</td>
            <td>${escapeHtml(s.lastName)}</td>
            <td>${escapeHtml(s.email)}</td>
            <td><span class="status-badge success">${escapeHtml(s.department || 'N/A')}</span></td>
            <td>${escapeHtml(s.phone || 'N/A')}</td>
            <td class="action-buttons">
                <button class="btn btn-warning btn-icon" onclick="editStudent(${s.id})" title="Edit">
                    <i class="fas fa-edit"></i>
                </button>
                <button class="btn btn-danger btn-icon" onclick="deleteStudent(${s.id})" title="Delete">
                    <i class="fas fa-trash"></i>
                </button>
            </td>
        </tr>
    `).join('');
}

// ---- Open Modal ----
function openModal() {
    isEditing = false;
    document.getElementById('modalTitle').innerHTML = '<i class="fas fa-user-plus"></i> Add New Student';
    document.getElementById('submitBtn').innerHTML = '<i class="fas fa-save"></i> Save Student';
    document.getElementById('studentForm').reset();
    document.getElementById('studentId').value = '';
    document.getElementById('studentModal').classList.add('active');
}

// ---- Close Modal ----
function closeModal() {
    document.getElementById('studentModal').classList.remove('active');
    document.getElementById('studentForm').reset();
}

// ---- Handle Form Submit ----
async function handleSubmit(event) {
    event.preventDefault();
    const student = {
        firstName: document.getElementById('firstName').value.trim(),
        lastName: document.getElementById('lastName').value.trim(),
        email: document.getElementById('email').value.trim(),
        department: document.getElementById('department').value,
        phone: document.getElementById('phone').value.trim()
    };

    try {
        let response;
        if (isEditing) {
            const id = document.getElementById('studentId').value;
            response = await fetch(`${API_BASE}/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(student)
            });
        } else {
            response = await fetch(API_BASE, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(student)
            });
        }

        const result = await response.json();
        if (result.success) {
            showAlert(isEditing ? 'Student updated successfully!' : 'Student added successfully!', 'success');
            closeModal();
            loadStudents();
            loadStats();
        } else {
            showAlert(result.error || 'Operation failed', 'danger');
        }
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

// ---- Edit Student ----
async function editStudent(id) {
    try {
        const response = await fetch(`${API_BASE}/${id}`);
        const result = await response.json();
        if (result.success) {
            const s = result.data;
            isEditing = true;
            document.getElementById('modalTitle').innerHTML = '<i class="fas fa-edit"></i> Edit Student';
            document.getElementById('submitBtn').innerHTML = '<i class="fas fa-save"></i> Update Student';
            document.getElementById('studentId').value = s.id;
            document.getElementById('firstName').value = s.firstName;
            document.getElementById('lastName').value = s.lastName;
            document.getElementById('email').value = s.email;
            document.getElementById('department').value = s.department || '';
            document.getElementById('phone').value = s.phone || '';
            document.getElementById('studentModal').classList.add('active');
        }
    } catch (error) {
        showAlert('Failed to load student details', 'danger');
    }
}

// ---- Delete Student ----
async function deleteStudent(id) {
    if (!confirm('Are you sure you want to delete this student?')) return;
    try {
        const response = await fetch(`${API_BASE}/${id}`, { method: 'DELETE' });
        const result = await response.json();
        if (result.success) {
            showAlert('Student deleted successfully!', 'success');
            loadStudents();
            loadStats();
        } else {
            showAlert(result.error || 'Delete failed', 'danger');
        }
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

// ---- Search Students ----
async function searchStudents() {
    const keyword = document.getElementById('searchInput').value.trim();
    if (keyword.length === 0) {
        loadStudents();
        return;
    }
    try {
        const response = await fetch(`${API_BASE}/search?keyword=${encodeURIComponent(keyword)}`);
        const result = await response.json();
        if (result.success) {
            renderStudents(result.data);
        }
    } catch (error) {
        console.error('Search error:', error);
    }
}

// ---- Show Alert ----
function showAlert(message, type = 'info') {
    const container = document.getElementById('alertContainer');
    const icons = { success: 'check-circle', danger: 'exclamation-circle', warning: 'exclamation-triangle', info: 'info-circle' };
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.innerHTML = `<i class="fas fa-${icons[type] || 'info-circle'}"></i> ${message}`;
    container.prepend(alert);
    setTimeout(() => alert.remove(), 4000);
}

// ---- Escape HTML ----
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

