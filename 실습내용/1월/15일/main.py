from flask import Flask, escape, request
import pickle

app = Flask(__name__)

#pickle.dump(db, './db.bin')
pickle.load('./db.bin')
db = {}
id_ = 0

@app.route('/hello')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi', methods=['POST', 'GET'])
def hi():
    name = request.args.get("name", "World")
    return {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleImage": {
                                "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
                                "altText": "보물상자입니다"
                            }
                        }
                    ]
                }
            }

@app.route('/users', methods=['POST'])
def create_user():
    global id_

    user_data = request.get_json()
    db[id_] = user_data

    id_ += 1

    return f'{id_-1}, 저장완료'

@app.route('/users/<int:user_id>', methods=['GET'])
def select_user(user_id):
    key = user_id
    error_msg = f'{key}는 없습니다.'

    return db.get(key, error_msg)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    del db[user_id]

    return f'{user_id}, 삭제완료'

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    saved_data = db[user_id]
    update_data = request.get_json()

    saved_data.update(update_data)

    return saved_data