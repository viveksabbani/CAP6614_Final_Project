# Vulnerable code with insecure session management

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    # No actual authentication check
    response = make_response('Logged in as ' + username)
    # Setting session ID directly from username
    response.set_cookie('session_id', username)
    return response

@app.route('/dashboard')
def dashboard():
    session_id = request.cookies.get('session_id')
    if session_id:
        return f'Welcome back, {session_id}!'
    else:
        return 'Please log in.', 401

if __name__ == '__main__':
    app.run()