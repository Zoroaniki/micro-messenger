from uuid import UUID



class Chat():
    id: UUID
    name: str
    participants: list[UUID]
    messages: list[Message]


