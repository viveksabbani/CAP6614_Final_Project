# Vulnerable code using insecure deserialization

import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/load', methods=['POST'])
def load_data():
    serialized_data = request.data
    # Untrusted data is deserialized without validation
    data = pickle.loads(serialized_data)
    return 'Data loaded successfully.'

if __name__ == '__main__':
    app.run()