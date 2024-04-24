import requests

def request_name(user_id: int):
    print("______________________________________________________________________")
    print(user_id)
    response = requests.get("http://0.0.0.0:8001/users/{}".format(user_id))
    print(response)
    #print(response.json())
    return response.text
