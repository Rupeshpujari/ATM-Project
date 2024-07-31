from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Example user data
user_data = {
    'username': '9494861776',
    'pin': '5542',
    'balance': 3000
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    pin = request.form['pin']
    if username == user_data['username'] and pin == user_data['pin']:
        return jsonify({'status': 'success', 'balance': user_data['balance']})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid username or PIN'})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = int(request.form['amount'])
    if amount <= user_data['balance']:
        user_data['balance'] -= amount
        return jsonify({'status': 'success', 'balance': user_data['balance']})
    else:
        return jsonify({'status': 'error', 'message': 'Insufficient funds'})

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = int(request.form['amount'])
    user_data['balance'] += amount
    return jsonify({'status': 'success', 'balance': user_data['balance']})

if __name__ == '__main__':
    app.run(debug=True)