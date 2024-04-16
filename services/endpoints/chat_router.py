from fastapi import APIRouter, Depends, HTTPException, Body
from uuid import UUID, uuid4
from services.chat_service.chat_service import ChatService
from services.chat_service.models.message import Message

chat_router = APIRouter(prefix='/chat', tags = ['Chat'])

@chat_router.get('/')
def get_messages(chat_service: ChatService = Depends(ChatService)):
    return chat_service.get_messages()

@chat_router.post('/{id}/read')
def read_message(id: UUID, chat_service: ChatService = Depends(ChatService)):
    try:
        chat_service.read .finish_delivery(id)
    except KeyError:
        raise HTTPException(404, f'Error {id} нет')
    except ValueError:
        raise HTTPException(400, f'Delivery with id={id} can\'t be finished')
@chat_router.get('/write/{message}')
def send_message(message: str, chat_service: ChatService = Depends(ChatService)):
    chat_service.send_message(Message(message, uuid4))
