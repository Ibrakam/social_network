from fastapi import Request

from pydantic import BaseModel
from typing import List, Dict

from database.userservice import register_user_db, check_user_data_db, check_user_password_db, change_user_data, \
    get_user_db

from api import app

import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def mail_checker(email):
    if re.fullmatch(regex, email):
        return True

    return False


class User(BaseModel):
    name: str
    mail: str
    phone_number: str
    password: str
    user_city: str


@app.post("/api/registration")
async def register_user(user: User):
    user_data = dict(user)
    mail_validation = mail_checker(user.mail)
    if mail_validation:
        try:
            reg_user = register_user_db(**user_data)
            return {'status': 1, 'user_id': reg_user}
        except Exception as e:
            return {'status': 0, 'message': e}
    return {'status': 0,'message': 'Invalid mail'}

@app.get('/api/user')
async def get_user(user_id: int):
    exact_user = get_user_db(user_id)

    return {'status': 1, 'message': exact_user}


@app.post('/api/login')
async def login_user(mail: str, password: str):
    mail_validation = mail_checker(mail)
    if mail_validation:
        login_checker = str(check_user_password_db(mail_validation, password))

        if login_checker.isdigit():
            return {'status': 1, 'user_id': int(login_checker)}

        return {'status': 0, 'message': login_checker}
    return {'status': 0, 'message': 'Invalid mail'}

@app.put('/api/change_profile')
async def change_user_profile(user_id: int, change_info: str, new_data: str):
    data = change_user_data(user_id, change_info, new_data)

    return {'status': 1, 'message': data}
