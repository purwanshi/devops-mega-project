from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}  

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if data['username'] in users:
        return jsonify({'message': 'User exists!'}), 400
    users[data['username']] = data['password']
    return jsonify({'message': 'User created!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if users.get(data['username']) == data['password']:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
