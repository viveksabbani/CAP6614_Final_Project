import os
import subprocess
import pickle
import hashlib
import random
import string
import jwt
import yaml
import requests
import xml.dom.minidom as minidom

from flask import Flask, request, redirect

# 1. Use of `eval` with user input (Code Injection)
def dangerous_eval():
    user_input = input("Enter some code to evaluate: ")
    result = eval(user_input)  # Vulnerable to code injection
    print(f"Result: {result}")

# 2. Hardcoded Cryptographic Keys (Hardcoded Secret)
SECRET_KEY = "my$ecretK3y!"  # Hardcoded secret key

def generate_token(data):
    token = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return token

# 3. Insecure Randomness (Weak Random Number Generator)
def insecure_random_string(length):
    random_str = ''
    for _ in range(length):
        random_str += random.choice('abcdefghijklmnopqrstuvwxyz')  # Predictable randomness
    return random_str

# 4. Insecure Hashing Algorithm (Weak Cryptographic Practice)
def insecure_hash(data):
    return hashlib.sha1(data.encode()).hexdigest()  # SHA1 is considered weak

# 5. Command Execution with User Input (Command Injection)
def run_system_command():
    command = input("Enter a system command to run: ")
    os.system(command)  # Unsafe execution of system command

# 6. Insecure Use of `pickle.load` (Insecure Deserialization)
def load_config(file_path):
    with open(file_path, 'rb') as file:
        config = pickle.load(file)  # Can execute arbitrary code during unpickling
    return config

# 7. Use of `input` in Python 2 (Security Issue in Python 2)
def python2_input():
    user_input = input("Enter something: ")  # In Python 2, input() is equivalent to eval(input())
    print(f"You entered: {user_input}")

# 8. HTTP Request without SSL Verification (SSL Certificate Verification Disabled)
def make_insecure_request(url):
    response = requests.get(url, verify=False)  # SSL verification is disabled
    return response.content

# 9. YAML Loading without Safe Loader (Insecure YAML Deserialization)
def load_yaml(yaml_str):
    data = yaml.load(yaml_str)  # Unsafe loading, should specify Loader=yaml.SafeLoader
    return data

# 10. XML Parsing with External Entities Enabled (XXE Vulnerability)
def parse_xml(xml_str):
    dom = minidom.parseString(xml_str)  # May allow external entity expansion
    return dom.getElementsByTagName('data')

# 11. Use of `subprocess.Popen` with Shell=True (Shell Injection)
def execute_with_popen():
    command = input("Enter command to execute: ")
    process = subprocess.Popen(command, shell=True)  # shell=True can be dangerous
    process.communicate()

# 12. Format String Vulnerability
def format_string():
    user_input = input("Enter your name: ")
    print("Hello, " + user_input)
    log_msg = "User %s has logged in" % user_input
    print(log_msg)

# 13. Open Redirect Vulnerability
app = Flask(__name__)

@app.route('/redirect')
def open_redirect():
    url = request.args.get('url')
    return redirect(url)  # Redirecting to user-supplied URL

if __name__ == "__main__":

    # 1. Code Injection via eval
    dangerous_eval()

    # 2. Hardcoded Secret Key
    print(generate_token({'user_id': 1}))

    # 3. Weak Randomness
    print(insecure_random_string(10))

    # 4. Weak Hashing Algorithm
    print(insecure_hash('password123'))

    # 5. Command Injection
    run_system_command()

    # 6. Insecure Deserialization with pickle
    config = load_config('config.pkl')

    # 7. Python 2 Input Vulnerability
    python2_input()

    # 8. Insecure HTTP Request
    content = make_insecure_request('https://example.com')

    # 9. Insecure YAML Deserialization
    data = load_yaml('!!python/object/apply:os.system ["ls"]')

    # 10. XML External Entity (XXE) Vulnerability
    parse_xml('<?xml version="1.0"?><!DOCTYPE data [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><data>&xxe;</data>')

    # 11. Shell Injection with subprocess.Popen
    execute_with_popen()

    # 12. Format String Vulnerability
    format_string()

    # 13. Open Redirect via Flask
    app.run(debug=True)
