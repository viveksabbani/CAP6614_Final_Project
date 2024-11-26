# Vulnerable code illustrating broken access control

from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

# Simulated user data
users = {
    'alice': {'password': 'alicepass', 'role': 'user'},
    'bob': {'password': 'bobpass', 'role': 'user'},
    'admin': {'password': 'adminpass', 'role': 'admin'}
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = users.get(username)
    if user and user['password'] == password:
        session['username'] = username
        return 'Logged in!'
    else:
        return 'Invalid credentials', 401

@app.route('/admin')
def admin_panel():
    # Missing proper access control check
    if 'username' in session:
        return f"Welcome to the admin panel, {session['username']}!"
    else:
        return 'Please log in first.', 401

if __name__ == '__main__':
    app.run()