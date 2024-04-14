from services.chat_service.models.chat import Chat
from services.chat_service.models.message import Message, MessageStatus
from uuid import UUID

from app.database import get_db
from services.chat_service.models import message, chat
from services.chat_service.db import chat_schema, messages_schema


messages = []
chats = []

class ChatRepo():
    db: Session

    def __init__(self):
        self.db = next(db)

    def create_chat(self, chat_name: str, partisipants: []):
        self.db.add(Base, Chat(name=chat_name, participants=partisipants))
        #chats.append(Chat)

    def get_all_messages(self, chat_id):
        return messages

    def get_messages_by_text(self, text: str):
        return [item for item in messages if text in item.message_body]
    
    def get_messages_by_user(self, user_id: UUID):
        return [item for item in messages if item.sender_uuid == user_id]

    def remove_message(self, message: Message):
        messages.remove(message)

    def send_message(self, message: Message):
        messages.append(message)

    def set_message_status(self, message: Message, status: MessageStatus):
        messages[messages.index(message)].message_status = status

    def update_message(self, message: Message, new_text: str):
        messages[messages.index(message)].message_body = nenw_text
