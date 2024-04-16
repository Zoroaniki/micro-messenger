from uuid import UUID, uuid4
from services.chat_service.models.message import Message
from dataclasses import dataclass

@dataclass
class Chat():
    id: UUID = uuid4
    name: str
    participants: list[UUID]
    messages: list[Message]


