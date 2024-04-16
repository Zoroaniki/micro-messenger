#from services.chat_service.chat_service import ChatService
from uuid import UUID, uuid4
from services.chat_service.models.message import Message
from fastapi import FastAPI
from services.endpoints.chat_router import chat_router

app = FastAPI(title="Title")
app.include_router(chat_router, prefix='/api')
if __name__ == "__main__":
    print("jopa")
