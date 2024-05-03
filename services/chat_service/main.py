#from services.chat_service.chat_service import ChatService
from flask import render_template, Flask, redirect, url_for, request
from flask_cors import CORS
from uuid import UUID, uuid4
from models.message import Message
from endpoints.chat_router import urls_blueprint
from db.database import db
from dotenv import load_dotenv, dotenv_values
import os


load_dotenv()

user = os.getenv("BD_USER_NAME")
password = os.getenv("BD_PASSWORD")
bd_name = os.getenv("CHAT_DB_NAME")
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ilfi:password@62.217.187.32:3306/chat_service_db?charset=utf8mb4&collation=utf8mb4_general_ci'
db.init_app(app)
app.register_blueprint(urls_blueprint, url_prefix='/api')
app.secret_key = 'your_secret_key'
CORS(app, supports_credentials=True)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
