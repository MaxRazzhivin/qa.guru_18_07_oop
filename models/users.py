"""
Создаем класс абстрацию пользователя
"""
from dataclasses import dataclass

from enum import Enum

# Назначаем константу на возраст из логики проверок

USER_ADULT_AGE = 18


class Status(Enum):
    student = "student"
    worker = "worker"

@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE

    # Метод для инициализации экземпляров класса, конструктор самого класса

    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    # Метод для сравнения экземпляров класса по содержимому, а не по hash

    # def __eq__(self, other):
    #     return (self.name == other.name,
    #             self.age == other.age,
    #             self.status == other.status,
    #             self. items == other.items)
    #
    # # Метод для вывода на печать или в дебаге об экземпляре класса
    #
    # def __repr__(self):
    #     return "User"

if __name__ == '__main__':
    # Oleg;16;student;book,pen,paper
    d = {"name": "Oleg",
         "age": 16,
         "status": "student",
         "items": ["book", "pen", "paper"]}

    oleg = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
    oleg2 = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
    olga = User(name="Olga", age=18, status=Status.worker, items=["book", "paper"])

    assert oleg == oleg2

    assert oleg.age == 16
    assert olga.age == 18

    olga.age += 1
    assert olga.age == 19


