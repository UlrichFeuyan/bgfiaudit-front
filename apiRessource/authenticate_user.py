import requests
from .endpointList import *


def authenticate_user(username, password):
    data = {'code_user': username, 'password': password}

    response = requests.post(loginUrl, data=data)

    if response.status_code == 200:
        token = response.json().get('token')
        return token
    else:
        return None
