from models import *
from repo import ChatRepo

class ChatService():
    chat_repo: ChatRepo


    def __init__(self):
        self.chat_repo = ChatRepo()

    def get_messages(self):
        return self.chat_repo.get_all_messages()

    def send_message(self, message: Message):
        self.chat_repo.send_message(message)
        

