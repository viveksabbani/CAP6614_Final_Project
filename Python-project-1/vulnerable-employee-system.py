import os
import sqlite3
import subprocess
import pickle
import base64
import hashlib
import json
from flask import Flask, request, jsonify, session, render_template_string
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.secret_key = "dev_secret_key_123"  # Vulnerability #1: Hardcoded secret key

# Database initialization
def init_db():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS employees
        (id INTEGER PRIMARY KEY, name TEXT, role TEXT, salary INTEGER)
    ''')
    conn.commit()
    conn.close()

# Custom template for employee display
TEMPLATE = """
<html>
    <body>
        <h1>Welcome {{user}}!</h1>
        <div>{{content}}</div>
    </body>
</html>
"""

def get_db():
    conn = sqlite3.connect('employees.db')
    return conn

# Vulnerability #2: SQL Injection
@app.route('/search', methods=['GET'])
def search_employees():
    name = request.args.get('name', '')
    conn = get_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM employees WHERE name LIKE '%{name}%'"  # SQL Injection vulnerability
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)

# Vulnerability #3: Command Injection
@app.route('/export', methods=['POST'])
def export_data():
    format_type = request.form.get('format', 'csv')
    filename = request.form.get('filename', 'export')
    command = f"cat employees.db > exports/{filename}.{format_type}"  # Command injection vulnerability
    os.system(command)
    return f"Data exported to {filename}.{format_type}"

# Vulnerability #4: Insecure Deserialization
@app.route('/import_data', methods=['POST'])
def import_data():
    data = request.form.get('data')
    if data:
        decoded = base64.b64decode(data)
        employee_data = pickle.loads(decoded)  # Insecure deserialization
        return f"Imported data for {employee_data['name']}"
    return "No data provided"

# Vulnerability #5: XSS (Cross-Site Scripting)
@app.route('/profile/<username>')
def user_profile(username):
    return render_template_string(TEMPLATE, user=username, content="Profile page")  # XSS vulnerability

# Vulnerability #6: Broken Access Control
@app.route('/admin/dashboard')
def admin_dashboard():
    if session.get('role') == 'admin':  # Missing proper authentication check
        return "Welcome to admin dashboard"
    return "Access denied"

# Vulnerability #7: XML External Entity (XXE) Injection
@app.route('/process_xml', methods=['POST'])
def process_xml():
    xml_data = request.data
    tree = ET.parse(xml_data)  # XXE vulnerability
    root = tree.getroot()
    return jsonify({"status": "processed"})

# Vulnerability #8: Weak Password Hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # Weak hashing algorithm

# Vulnerability #9: Information Exposure
@app.errorhandler(Exception)
def handle_error(error):
    return str(error), 500  # Exposing detailed error messages

# Vulnerability #10: Insecure Direct Object References (IDOR)
@app.route('/employee/<id>/salary')
def get_salary(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT salary FROM employees WHERE id = {id}")  # IDOR vulnerability
    salary = cursor.fetchone()
    conn.close()
    return jsonify({"salary": salary[0] if salary else None})

# Seemingly Vulnerable but Actually Secure Pattern #1:
# This looks like SQL injection but uses parameterized queries
@app.route('/secure_search', methods=['GET'])
def secure_search():
    name = request.args.get('name', '')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    conn.close()
    return jsonify(results)

# Seemingly Vulnerable but Actually Secure Pattern #2:
# Looks like command injection but uses safe subprocess
@app.route('/secure_export', methods=['POST'])
def secure_export():
    filename = request.form.get('filename', 'export')
    if not filename.isalnum():
        return "Invalid filename"
    
    subprocess.run(['cp', 'employees.db', f'exports/{filename}.db'],
                  capture_output=True, text=True, check=True)
    return f"Data exported to {filename}.db"

# Seemingly Vulnerable but Actually Secure Pattern #3:
# Looks like it might leak sensitive data but actually validates authorization
@app.route('/api/employee/<id>')
def get_employee_details(id):
    if not session.get('user_id'):
        return jsonify({"error": "Unauthorized"}), 401
        
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, role FROM employees WHERE id = ?", (id,))
    employee = cursor.fetchone()
    conn.close()
    
    if not employee:
        return jsonify({"error": "Not found"}), 404
        
    return jsonify({
        "id": employee[0],
        "name": employee[1],
        "role": employee[2]
    })

# Additional secure routes for comparison
@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    required_fields = ['name', 'role', 'salary']
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
        
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)",
        (data['name'], data['role'], data['salary'])
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400
        
    # Actual login logic would go here
    session['user_id'] = 1
    session['role'] = 'user'
    return jsonify({"status": "logged in"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)  # Additional vulnerability: Debug mode enabled in production
