import pytest
import requests
from Contact_services import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/poisk')
    assert response.status_code == 500

def test_friends(client):
    response = client.get('/friends')
    assert response.status_code == 500

def test_give_user_name(client):
    response = client.get('/users/1')
    assert response.status_code == 500

def test_ilya(client):
    response = client.post('/test/1')
    assert response.status_code == 500

