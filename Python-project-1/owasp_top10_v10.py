# Vulnerable code allowing SSRF

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_url():
    target_url = request.args.get('url')
    # Fetch content from user-supplied URL without validation
    response = requests.get(target_url)
    return response.content

if __name__ == '__main__':
    app.run()