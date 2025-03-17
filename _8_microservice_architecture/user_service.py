from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store (Replace with a database in a real-world scenario)
users = {}
user_id_counter = 3

@app.route("/register", methods=["POST"])
def register():
    global user_id_counter

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username are required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id_counter] = {
        "username": username
    }
    response = {"message": "User created", "user_id": user_id_counter}
    user_id_counter += 1

    return jsonify(response), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(port=5001, debug=True)
