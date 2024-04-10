from services.chat_service.chat_service import ChatService
from uuid import UUID, uuid4
from services.chat_service.models.message import Message
if __name__ == "__main__":
    service = ChatService()

    service.send_message(Message(sender_id = "Hui", message_body = uuid4()))
    print(service.get_messages())
