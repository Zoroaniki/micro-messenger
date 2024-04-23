from uuid import UUID, uuid4
from models.message import Message
from dataclasses import dataclass

class Chat():
    id: UUID = uuid4
    name: str
    participants: list[UUID]
    messages: list[Message]


