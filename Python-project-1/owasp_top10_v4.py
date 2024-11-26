# Vulnerable code with insecure password reset functionality

from flask import Flask, request

app = Flask(__name__)

# Simulated user database
users = {'user1': 'user1@example.com'}

def send_password_reset_email(email):
    # Dummy function to simulate sending email
    print(f"Sending password reset email to {email}")

@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form['email']
    # Not verifying if the email exists in the database
    send_password_reset_email(email)
    return 'If that email is registered, a reset link has been sent.'

if __name__ == '__main__':
    app.run()