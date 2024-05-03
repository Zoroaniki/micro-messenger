from fastapi import APIRouter, Depends, HTTPException, Body
from flask import Blueprint, request, redirect, session
from uuid import UUID, uuid4
from repo.chat_repo import ChatRepo
from models.message import Message, MessageStatus
from db.messages_schema import MessageTable
from requests_dir.requester import request_uuid
import datetime
import sys
import os
from dotenv import load_dotenv, dotenv_values
import json

load_dotenv()
urls_blueprint = Blueprint('chat', __name__,)

redirect_address = os.getenv("REDIRECT_ADDRESS")
chat_repo = ChatRepo()

@urls_blueprint.route('/<id>', methods=['POST', 'GET'])
def get_messages(id: int):

    auth = session.get('uuid')
    print("XDDDD: {}".format(auth), file=sys.stderr)
    users = chat_repo.get_users_by_chat_id(int(id))
    print(users, file=sys.stderr)
    current_user = -1
    for user in users:
        print("XDDDD2: {}".format(request_uuid(user["id"])), file=sys.stderr)
        request_result_dict = json.loads(request_uuid(user["id"]))
        print("XDDDD3: {}".format(request_result_dict), file=sys.stderr)
        if auth == request_result_dict["uuid"]:
            current_user = user
            break

    if current_user == -1 and int(id) != 0:
        raise HTTPException(403, f'#Нет доступа к этому чату!')

    if request.method == 'POST':
        message = request.form['message']
        if current_user == -1:
            current_user = -1
        else:
            current_user = current_user["id"]

        message_table = MessageTable( message_body=message, sender_id=current_user, chat_id=id, message_status=MessageStatus.SENT, send_time=datetime.datetime.now())
        print("message_table: {}".format(message_table), file=sys.stderr)
        chat_repo.send_message(message_table)
        return chat_repo.get_all_messages(id)
    else:
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


@urls_blueprint.route('/back_to_friends')
def go_back_from_chat():
    print("redirect:{}".format(redirect_address), file=sys.stderr)
    return redirect("{}:8001/friends".format(redirect_address), code=301)

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

@urls_blueprint.route('/create_chat', methods=['POST'])
def create_chat():
    users = request.args.getlist('user', type=int)
    print("users")
    print(users)
    chat_name = request.args.get('name', type=str)
    chat_repo.create_chat(chat_name=chat_name, partisipants=users)
    return "it worked"

