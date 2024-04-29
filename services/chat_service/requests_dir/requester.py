import requests
import os
from dotenv import load_dotenv, dotenv_values


redirect_address = os.getenv("REDIRECT_ADDRESS")

load_dotenv()

def request_name(user_id: int):
    print("______________________________________________________________________")
    print(user_id)
    response = requests.get("{}:8001/users/{}".format(redirect_address, user_id))
    print(response)
    #print(response.json())
    return response.text

def request_uuid(user_id: int):
    response = requests.get("{}:8002/user/{}/uuid".format(redirect_address, user_id))
    return response.text
