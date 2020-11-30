from flask import Flask, jsonify
from users import users

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/users')
def getUsers():
    return jsonify(users)

@app.route('/users/<string:id>')
def getUser(id):
    userFound = [user for user in users if user.get('user_id') == id]

    if len(userFound) > 0:
        return jsonify(userFound[0])

    return jsonify({"message": "No user found with ID " + id})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
