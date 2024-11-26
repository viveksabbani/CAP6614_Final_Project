# Vulnerable code with debug mode enabled

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True  # Debug mode should not be enabled in production

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()