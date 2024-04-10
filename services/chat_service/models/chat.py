from uuid import UUID
from services.chat_service.models.message import Message



class Chat():
    id: UUID
    name: str
    participants: list[UUID]
    messages: list[Message]


