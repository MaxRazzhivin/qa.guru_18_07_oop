"""
Прямолинейный вариант теста
"""
import csv


def test_workers_are_adults():
    """
    Тестируем, что все работники старше 18 лет
    """

    with open("users.csv") as f:
        users = csv.DictReader(f, delimiter=";")
        workers = [user for user in users if user["status"] == "worker"]

        # Аналог list comprehensions, но для словарей dict comprehensions

        # {key: value for key, value in some_dict.items() if ... }

    for worker in workers:
        assert int(worker['age']) >= 18, f'Worker {worker['name']} младше 18 лет'
