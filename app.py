from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)


class User:
    def __init__(self, firstName, email):
        self.id = str(uuid.uuid4())
        self.firstName = firstName
        self.email = email

    def to_dict(self):
        pass


users_list = []

user1 = User("User1", "user1@gmail.com")
users_list.append(user1.__dict__)
user2 = User("User2", "user2@gmail.com")
users_list.append(user1.__dict__)


@app.route('/users', methods=['GET'])
def get_users():
    response = {
        "message": "Users retrieved",
        "success": True,
        "users": users_list
    }
    return jsonify(response), 200


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    for user in users_list:
        if user.get("id") == id:
            return jsonify({
                'success': True,
                'user': user
            }), 200
    return jsonify({
        "success": False,
        "message": "User not found."
    }), 404


@app.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    if data.get("firstName") and data.get("email"):
        user = User(data.get("firstName"), data.get("email"))
        users_list.append(user.__dict__)
        return jsonify({
            "message": "User added",
            "success": True
        }), 200
    return jsonify({
        "success": False,
        "message": "Error while creating user."
    }), 404


@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    if data.get("firstName") or data.get("email"):
        for i in range(len(users_list)):
            if users_list[i]['id'] == id:
                if data.get('firstName'):
                    users_list[i]['firstName'] = data.get('firstName')
                if data.get('email'):
                    users_list[i]['email'] = data.get('email')
                return jsonify({
                    "message": "User updated",
                    "success": True
                }), 200
    return jsonify({
        "message": "User not found.",
        "success": False
    }), 404
