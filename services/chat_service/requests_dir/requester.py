import requests

def request_name(user_id: int):
    response = requests.get("http://0.0.0.0:8001/users/{}".format(user_id))
    print(response.json())
    return response.json()
