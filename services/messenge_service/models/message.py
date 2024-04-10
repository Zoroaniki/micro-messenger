from datetime import datetime
from uuid import UUID



class MessageStatus(enum.Enum):
    SENT = "sent"
    RECIEVED = "recieved"
    READ = "read"
    ERROR = "error"

class Message():
    sender_id: UUID
    chat_id: UUID
    message_body: str
    message_status: Message_status
    send_time: datetime


class MediaMessage(Message):
    media: Media
