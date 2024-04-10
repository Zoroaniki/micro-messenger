from services.chat_service.models.chat import Chat
from services.chat_service.models.message import Message
from services.chat_service.repo.chat_repo import ChatRepo

class ChatService():
    chat_repo: ChatRepo


    def __init__(self):
        self.chat_repo = ChatRepo()

    def get_messages(self):
        return self.chat_repo.get_all_messages()

    def send_message(self, message: Message):
        self.chat_repo.send_message(message)
        

