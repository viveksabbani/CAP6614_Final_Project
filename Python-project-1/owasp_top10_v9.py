# Vulnerable code with insufficient logging

from flask import Flask, request

app = Flask(__name__)

@app.route('/transfer', methods=['POST'])
def transfer_money():
    sender = request.form['sender_account']
    recipient = request.form['recipient_account']
    amount = request.form['amount']
    # Perform transfer (details omitted)
    return 'Transfer completed.'

if __name__ == '__main__':
    app.run()