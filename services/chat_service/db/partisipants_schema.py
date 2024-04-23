from sqlalchemy import Column, String, DateTime, Enum, Integer
from models.message import MessageStatus
from db.base_schema import Base
from db.database import engine



class PartisipantsTable(Base):
    __tablename__ = 'partisipants'
    id = Column(Integer, primary_key=True)
    message_body = Column(String(255), nullable=True)
    sender_id = Column(Integer, nullable=False)
    chat_id = Column(Integer, nullable=False)
    message_status = Column(Enum(MessageStatus), nullable=False)
    send_time = Column(DateTime, nullable=False)


#Base.metadata.create_all(engine)
