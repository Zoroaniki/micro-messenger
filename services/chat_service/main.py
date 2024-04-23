#from services.chat_service.chat_service import ChatService
from flask import render_template, Flask, redirect, url_for, request
from uuid import UUID, uuid4
from models.message import Message
from fastapi import FastAPI
from endpoints.chat_router import urls_blueprint
from db.database import db

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ilfi:password@localhost/chat_service_db?charset=utf8mb4&collation=utf8mb4_general_ci'
db.init_app(app)
app.register_blueprint(urls_blueprint, url_prefix='/api')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
