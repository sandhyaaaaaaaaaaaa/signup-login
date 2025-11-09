from flask import Flask, request, jsonify  # Fix: 'Flask' should be lowercase 'flask'

app = Flask(__name__) 

# Simple in-memory "database"
import json, os

users_file = "users.json"

# Load existing users
if os.path.exists(users_file):
    with open(users_file, "r") as f:
        users = json.load(f)
else:
    users = {}

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get("sandhya")
    password = data.get("1234")
    if username in users:
        return jsonify({"message": "Username already exists"}), 400

    users[username] = password
    with open(users_file, "w") as f:
        json.dump(users, f)
    return jsonify({"message": "Signup successful!"}), 201



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        username = request.args.get("username")
        password = request.args.get("password")
    else:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
    
    if username not in users:
        return jsonify({"message": "User not found"}), 404

    if users[username] != password:
        return jsonify({"message": "Invalid password"}), 401

    return jsonify({"message": f"Welcome back, {username}!"}), 200


if __name__ == '__main__':  # Fix: '__main__' instead of '_main_'
    app.run(debug=True)