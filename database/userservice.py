from database.models import User
from datetime import datetime

from database import get_db


def register_user_db(name, mail, phone_number, password, user_city):
    db = next(get_db())

    new_user = User(name=name, mail=mail, phone_number=phone_number,
                    password=password, user_city=user_city,
                    reg_date=datetime.now())

    db.add(new_user)
    db.commit()

    return new_user.id

def check_user_data_db(phone_number, mail):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number, mail=mail).first()

    if checker:
        return False

    return True

def check_user_password_db(mail, password):
    db = next(get_db())

    checker = db.query(User).filter_by(mail=mail).first()

    if checker:
        if checker.password == password:
            return checker.id

        else:
            return 'Неверный пароль'

    return 'Неверная почта'


def get_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    if exact_user:
        return exact_user.mail, \
            exact_user.phone_number, exact_user.id, \
            exact_user.name, exact_user.reg_date, exact_user.user_city

    return 'Пользователь не найден'


def change_user_data(user_id, change_info, new_data):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    if exact_user:
        if change_info == 'mail':
            exact_user.mail = new_data
        elif change_info == 'number':
            exact_user.phone_number = new_data
        elif change_info == 'name':
            exact_user.name = new_data
        elif change_info == 'city':
            exact_user.user_city = new_data
        elif change_info == 'password':
            exact_user.password = new_data

        db.commit()

        return 'Данные успешно изменены'

    return 'Пользователь не найден'





























