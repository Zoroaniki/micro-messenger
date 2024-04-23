#from services.chat_service.chat_service import ChatService
from flask import render_template, Flask, redirect, url_for, request
from uuid import UUID, uuid4
from models.message import Message
from fastapi import FastAPI
from endpoints.chat_router import urls_blueprint
from db.database import db

app = Flask(__name__, template_folder='services/chat_service/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ilfi:password@localhost/chat_service_db?charset=utf8mb4&collation=utf8mb4_general_ci'
db.init_app(app)
app.register_blueprint(urls_blueprint, url_prefix='/api')

with app.app_context():
    db.create_all()
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
    print("jopa")
