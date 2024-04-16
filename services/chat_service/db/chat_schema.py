from sqlalchemy import Column, String, DateTime, Enum, Integer
from services.chat_service.db.base_schema import Base
from services.chat_service.db.database import engine



class ChatTable(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    partisipants = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
