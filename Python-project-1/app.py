# app.py
import os
import sqlite3
import hashlib
import pickle
import requests
from flask import Flask, request, session, redirect, url_for, render_template, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Hardcoded secret key (Vulnerability)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Initialize database connection (Vulnerable and Outdated Components)
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL
)
''')
conn.commit()

# Insert sample users
users = [
    ('alice', hashlib.md5('password123'.encode()).hexdigest(), 'user'),
    ('bob', hashlib.md5('password123'.encode()).hexdigest(), 'user'),
    ('admin', hashlib.md5('adminpass'.encode()).hexdigest(), 'admin')
]

for user in users:
    try:
        cursor.execute('INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)', user)
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # User already exists

# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Weak password hashing (Cryptographic Failures)
        password_hash = hashlib.md5(password.encode()).hexdigest()

        # SQL Injection vulnerability (Injection)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password_hash = '{password_hash}'"
        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            session['username'] = username
            # Insecure session management (Identification and Authentication Failures)
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('session_id', username)
            return response
        else:
            return 'Invalid credentials', 401
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        # Broken access control
        if username == 'admin':
            return render_template('admin.html')
        else:
            return f'Welcome, {username}! You are logged in.'
    else:
        return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Unrestricted file upload
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'
    else:
        return render_template('upload.html')

@app.route('/deserialize', methods=['POST'])
def deserialize_data():
    # Insecure deserialization (Software and Data Integrity Failures)
    data = request.data
    obj = pickle.loads(data)
    return 'Data deserialized'

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    # SSRF vulnerability
    response = requests.get(url)
    return response.content

@app.route('/config')
def show_config():
    # Exposing sensitive information (Security Misconfiguration)
    return str(app.config)

@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form['email']
    # Insecure design (revealing user existence)
    if email == 'user@example.com':
        return 'Password reset link sent to your email.'
    else:
        return 'Email not registered.'

@app.route('/transfer', methods=['POST'])
def transfer():
    sender = request.form['from_account']
    recipient = request.form['to_account']
    amount = request.form['amount']
    # No security logging and monitoring
    # Process the transfer (details omitted)
    return 'Transfer completed successfully.'

if __name__ == '__main__':
    # Debug mode enabled (Security Misconfiguration)
    app.run(debug=True, host='0.0.0.0')