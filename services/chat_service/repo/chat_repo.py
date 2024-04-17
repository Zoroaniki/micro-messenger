from services.chat_service.models.chat import Chat
from services.chat_service.models.message import Message, MessageStatus
from uuid import UUID
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from flask import render_template, request
from flask import jsonify
import json
import sqlalchemy
import datetime
from services.chat_service.models import message, chat
from services.chat_service.db.chat_schema import ChatTable
from services.chat_service.db.messages_schema import MessageTable
from services.chat_service.db import chat_schema, messages_schema

from services.chat_service.db.database import db



class ChatRepo():

    def __init__(self):
        #engine = db.create_engine('mysql://root:icf192994lsS@localhost/chat_service_db')
        print("start")
        #new_message = MessageTable(id=1, message_body="chel", sender_id=1, chat_id=1, message_status=MessageStatus.SENT, send_time=datetime.datetime.now())
        #self.db.add(new_message)
        #self.db.commit()

    def create_chat(self, chat_name: str, partisipants: []):
        self.db.add(Base, Chat(name=chat_name, participants=partisipants))
        self.db.commit()
        #chats.append(Chat)

    def get_all_messages(self, chat_id):
        #ass = self.db.query(messages_schema.MessageTable)
        messages = MessageTable.query.filter(MessageTable.chat_id == chat_id)

        jason = [{
            'id': message.id,
            'message_body': message.message_body,
            'sender_id': message.sender_id,
            'chat_id': message.chat_id,
            'message_status': message.message_status.value if message.message_status else None,
            'send_time': message.send_time.isoformat() if message.send_time else None
        } for message in messages]
        return render_template("index.html", messages=jason)

    def get_messages_by_text(self, text: str):
        return [item for item in messages if text in item.message_body]
    
    def get_messages_by_user(self, user_id: UUID):
        return [item for item in messages if item.sender_uuid == user_id]

    def set_message_status(self, message: Message, status: MessageStatus):
        messages[messages.index(message)].message_status = status

    def send_message(self, message: MessageTable):
        db.session.add(message)
        db.session.commit()

    def create_chat(self, chat_name: str, partisipants = [int]):
        self.chat_repo.create_chat(chat_name, partisipants)
    
    def delete_message(self, chat_id: int, message_id: int):
        to_delete = self.db.query(MessageTable).filter(MessageTable.chat_id == chat_id and MessageTable.id == message_id)
        to_delete.delete()
        self.db.commit()

    def edit_message(self, chat_id: int, message_id: int, new_text: str):
        to_update = self.db.query(MessageTable).filter(MessageTable.chat_id == chat_id and MessageTable.id == message_id)
        to_update.update({'message_body': new_text})
        self.db.commit()

    def add_contact(self, chat_id: int, contact_id: int):
        self.chat_repo.add_contact(self, chat_id, contact_id)

    def get_partisipants(self, chat_id: int):
        return self.chat_repo.get_partisipants(chat_id)

