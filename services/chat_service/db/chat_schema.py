from sqlalchemy import Column, String, DateTime, Enum, Integer


from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db.database import db


class ChatTable(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) 
    name: Mapped[str] = mapped_column(String(255))


#Base.metadata.create_all(engine)
