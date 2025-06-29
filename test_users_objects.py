"""
Используем объектный подход работы с данными
"""
import csv

import pytest

from models.users import User, USER_ADULT_AGE, Status


@pytest.fixture
def users() -> list[User]:
    with open('users.csv') as f:
        users = list(csv.DictReader(f, delimiter=";"))
    return [
        User(name=user["name"],
             age=int(user['age']),
             status=user['status'],
             items=user['items'])
        for user in users
    ]


@pytest.fixture
def workers(users) -> list[User]:
    '''
    Берем только работников из списка пользователей
    '''

    workers = [user for user in users if user.status == Status.worker]
    return workers

def test_workers_are_adult_v3(workers):
    '''
    Тестируем, что все работники старше 18 лет
    '''

    for worker in workers:
        assert worker.is_adult(), f'Worker {worker.name} младше {USER_ADULT_AGE} лет'



