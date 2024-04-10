from datetime import datetime
from uuid import UUID, uuid4
from dataclasses import dataclass
import enum



class MessageStatus(enum.Enum):
    SENT = "sent"
    RECIEVED = "recieved"
    READ = "read"
    ERROR = "error"


@dataclass
class Message():
    sender_id: UUID
    message_body: str
    chat_id: UUID = uuid4()
    message_status: MessageStatus = MessageStatus.SENT
    send_time: datetime = datetime.now()

