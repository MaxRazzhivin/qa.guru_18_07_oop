"""
Используем объектный подход работы с данными
"""
import csv

import pytest

from models.providers import UserProvider, CsvUserProvider
from models.users import User, USER_ADULT_AGE, Status, Worker

@pytest.fixture()
def user_provider() -> UserProvider:
    return CsvUserProvider()


@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture
def workers(users) -> list[Worker]:
    '''
    Берем только работников из списка пользователей
    '''

    workers = [Worker(name=user.name, age=user.age,items=user.items)
               for user in users if user.status == Status.worker]
    return workers

def test_workers_are_adult_v3(workers):
    '''
    Тестируем, что все работники старше 18 лет
    '''

    for worker in workers:
        assert worker.is_adult(), f'Worker {worker.name} младше {USER_ADULT_AGE} лет'



