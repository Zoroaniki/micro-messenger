import requests

def request_name(user_id: int):
    response = requests.get("192.168.1.75:8001/user/{}".format(user_id))
    print(response.json())
    return response.json()
