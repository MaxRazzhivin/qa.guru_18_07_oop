import csv

import pytest

"""
Используем функциональный подход
Выносим логику в отдельные функции или фикстуры

Суть в том, чтобы в тесте оставить только проверку assert

Остальное выносим в фикстуры - открытие файла и фильтрация работников
"""

@pytest.fixture
def users():
    with open("users.csv") as f:
        users = list(csv.DictReader(f, delimiter=";"))
    return users

@pytest.fixture
def workers(users):
    """
    Берем только работников из списка пользователей
    """
    workers = [user for user in users if user["status"] == "worker"]
    return workers

def test_workers_are_adults_v2(workers):
    """
    Тестируем, что всем работникам больше либо равно 18 лет
    """
    for worker in workers:
        assert user_is_adult(worker), f"Worker {worker['name']} младше 18 лет"

def user_is_adult(user):
    return int(user["age"]) >= 18
