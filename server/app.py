from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods=['GET'])
def get_all_messages():
    messages = Message.query.all()
    return jsonify({'messages': [message.serialize() for message in messages]})

@app.route('/messages/<int:id>', methods=['GET'])
def get_message_by_id(id):
    message = Message.query.get(id)
    if message:
        return jsonify(message.serialize())
    else:
        return jsonify({'error': 'Message not found'}), 404

@app.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    new_message = Message(content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.serialize()), 201

@app.route('/messages/<int:id>', methods=['PUT'])
def update_message(id):
    message = Message.query.get(id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    
    data = request.get_json()
    message.content = data['content']
    db.session.commit()
    return jsonify(message.serialize())

@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    message = Message.query.get(id)
    if not message:
        return jsonify({'error': 'Message not found'}), 404
    
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message deleted successfully'})

if __name__ == '__main__':
    app.run(port=5555)
