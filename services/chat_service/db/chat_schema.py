from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.mysql import UUID
from services.chat_service.db.base_schema import Base



class ChatTable(Base):
    __tablename__ = 'chats'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    partisipants = Column(UUID(as_uuid=True), nullable=False)
