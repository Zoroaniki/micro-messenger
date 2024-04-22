from fastapi import APIRouter, Depends, HTTPException, Body
from flask import Blueprint, request, redirect
from uuid import UUID, uuid4
from services.chat_service.repo.chat_repo import ChatRepo
from services.chat_service.models.message import Message, MessageStatus
from services.chat_service.db.messages_schema import MessageTable
import datetime

urls_blueprint = Blueprint('chat', __name__,)

chat_repo = ChatRepo()

@urls_blueprint.route('/<id>', methods=['POST', 'GET'])
def get_messages(id: int):
    if request.method == 'POST':
        message = request.form['message']
        message_table = MessageTable( message_body=message, sender_id=2, chat_id=id, message_status=MessageStatus.SENT, send_time=datetime.datetime.now())
        chat_repo.send_message(message_table)
        return chat_repo.get_all_messages(id)
    else:
        print("got here")
        return chat_repo.get_all_messages(id)

@urls_blueprint.route('/messages', methods=['GET'])
def get_messages2():
    return chat_repo.get_all_messages2()

@urls_blueprint.route('/')
def get_all_messages():
    return chat_repo.get_all_messages()

@urls_blueprint.route('/<chat_id>/delete/<message_id>')
def delete_message(chat_id: int, message_id: int):
    chat_repo.delete_message(chat_id, message_id)

@urls_blueprint.route('/get_chats/<user_id>')
def get_chats_by_id_user_id(user_id: int):
    return chat_repo.get_chats(user_id)

@urls_blueprint.route('/{id}/read')
def read_message(id: int):
    try:
        chat_repo.get_messages(id)
    except KeyError:
        raise HTTPException(404, f'Error {id} нет')
    except ValueError:
        raise HTTPException(400, f'Delivery with id={id} can\'t be finished')

@urls_blueprint.route('/{id}/write/{message}')
def send_message(chat_id: int, message: str):
    if request.method == 'POST':
        message = request.form['message']
        message_table = MessageTable(2, "Soobshenia", 2, 3, datetime.datetime.now())
        chat_repo.send_message(message)
    else:
        return redirect(url_for('api/{}').format(chat_id))

@urls_blueprint.route('/create_chat', methods=['GET'])
def create_chat():
    users = request.args.getlist('user', type=int)
    print("users")
    print(users)
    chat_name = request.args.get('name', type=str)
    chat_repo.create_chat(chat_name=chat_name, partisipants=users)
    return "it worked"

