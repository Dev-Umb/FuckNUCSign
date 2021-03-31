import requests

from config.config import *


def fuck_nuc_course(session, course):
    for i in course:
        uri = sign_url + i['id']
        result = session.get(uri).json()['data']
        print(session.headers['username']+':'+i['name'] + result+"\n")


def login(account, password='123456'):
    session = requests.session()
    body = session.post(url=url, json={
        "username": account,
        "password": password,
        "client": "WAP_BROWSER",
        "customer": "STUDENT"
    })
    print(body.json())
    jwt = body.json()['data']
    uri = login_url + f'token={jwt}'
    session.headers = {
        "username": account,
        "password": password,
        "Authorization": jwt
    }
    session.get(uri)
    return session
