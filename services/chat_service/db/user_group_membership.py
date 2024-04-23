from sqlalchemy import Table, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import db
from sqlalchemy.orm import Mapped, mapped_column

class UserChatAssociation(db.Model):
    __tablename__ = 'user_chat_association'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat_table.id'), primary_key=True)


class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True) 

