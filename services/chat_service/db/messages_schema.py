from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.mysql import UUID
from services.chat_service.models.message import MessageStatus

class MessageTable(Base):
    __tablename__ = 'messages'
    id = Column(UUID(as_uuid=True), primary_key=True)
    message_body = Column(String, nullable=True)
    sender_id = Column(UUID(as_uuid=True), nullable=False)
    message_status = Column(Enum(MessageStatus), nullable=False)
    send_time = Column(DateTime, nullable=False)
