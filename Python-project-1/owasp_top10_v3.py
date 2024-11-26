# Vulnerable code susceptible to SQL injection

import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # User input directly included in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

@app.route('/user')
def user_profile():
    username = request.args.get('username')
    user_data = get_user_data(username)
    return str(user_data)

if __name__ == '__main__':
    app.run()