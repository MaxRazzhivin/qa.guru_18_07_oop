# Основы Python. Часть III. Применение ООП в написании автотестов.

```bash
Инкапсуляция - Самодокументируемость кода, а так же соблюдение принципов вроде DRY и KISS позволяет 
избежать дублирования кода и упростить его поддержку.

Скрытие внутренней реализации от пользователя и предоставление только нужного интерфейса.
Ты создаёшь класс, у которого есть внутренние данные и методы, и ты не хочешь, чтобы пользователь их трогал напрямую. 
Ты даёшь пользователю удобный внешний интерфейс, а внутренности прячешь.
```

```bash
Объектный подход - абстракция

Класс - это абстракция, которая описывает поведение и состояние объекта. 
Экземпляр - это конкретный объект, который создан на основе класса.
```

```bash
Наследование

Наследование позволяет создавать новые классы на основе уже существующих. 
Новый класс может расширять функциональность существующего, а так же переопределять его поведение.
```

```bash
Полиморфизм
Полиморфизм позволяет использовать один и тот же интерфейс для разных типов объектов.
```

```bash
Модули и классы
Файлы и папки в Python - это модули. Модули могут содержать в себе функции, классы, переменные и другие объекты.
```


# Пошаговые итерации от обычного теста к структуре с ООП

```bash
1) Обычный тест на прочтение файлика из .csv и фильтрацию пользователей из него: 
- на статус worker
- на совершеннолетие 18+ лет

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

```
```bash
2) Оставим в тесте только шаги самой проверки assert, остальное вынесем в фикстуры - подготовка тестовых данных

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


Отдельно вынесли в функцию проверку на возраст:

def user_is_adult(user):
    return int(user["age"]) >= 18

```


# 3. Применяем объектный подход. Создание класса и его экземпляра с методами

```bash
"""
Создаем класс абстрацию пользователя
"""

а) Делаем новый класс User, дальше каждый новый пользователь будет абстракцией к нему
  - создаем директорию models->users.py для наших классов 
  - компоненты, которые будут внутри класса User берем из файлика .csv, т.е. это будут
  name, age, status, items


class User:
    name: str
    age: int
    status: str
    items: list[str]

    Метод для инициализации экземпляров класса, конструктор самого класса

    def __init__(self, name, age, status, items):
        self.name = name
        self.age = age
        self.status = status
        self.items = items

    Метод для сравнения экземпляров класса по содержимому, а не по hash

    def __eq__(self, other):
        return (self.name == other.name,
                self.age == other.age,
                self.status == other.status,
                self. items == other.items)

    Метод для вывода на печать или в дебаге об экземпляре класса

    def __repr__(self):
        return "User"

if __name__ == '__main__':
    # Oleg;16;student;book,pen,paper
    d = {"name": "Oleg",
         "age": 16,
         "status": "student",
         "items": ["book", "pen", "paper"]}
         
    oleg = User(name="Oleg", age=16, status="student", items=["book", "pen", "paper"])
    oleg2 = User(name="Oleg", age=16, status="student", items=["book", "pen", "paper"])
    olga = User(name="Olga", age=18, status="worker", items=["book", "paper"])

    assert oleg == oleg2

    assert oleg.age == 16
    assert olga.age == 18

    olga.age += 1
    assert olga.age == 19

```

## Всю эту запись выше можно сократить через специальный dataclass

```bash
from dataclasses import dataclass

Далее мы просто дописываем декоратор над классом:
@dataclass
```

```bash
Что нам позволяет этот декоратор? 

Мы можем не писать методы __init__, __eq__ и ряд других, они уже внутри декоратора
Поэтому оставляем только начало создания абстрации и убираем методы

@dataclass
class User:
    name: str
    age: int
    status: str
    items: list[str]
```

