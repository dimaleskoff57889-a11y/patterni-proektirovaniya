"""Тема 5. Классы: определение, атрибуты экземпляра и класса."""


class Dog:
    """Задание 25. Класс Dog.

    Конструктор принимает имя (name) и породу (breed) и сохраняет их
    как атрибуты экземпляра. Метод bark() возвращает строку
    "Гав! Я {name}, порода {breed}".

    Примеры:
        dog = Dog("Рекс", "овчарка")
        dog.name == "Рекс"
        dog.breed == "овчарка"
        dog.bark() == "Гав! Я Рекс, порода овчарка"
    """

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"Гав! Я {self.name}, порода {self.breed}"


class Robot:
    """Задание 26. Атрибут класса: общий счётчик.

    Атрибут КЛАССА count хранит общее число созданных роботов и увеличивается
    в __init__. Каждый робот получает серийный номер serial — значение
    счётчика на момент его создания (1, 2, 3, ...).

    Внимание: атрибут count должен быть ОБЩИМ для класса (доступен как
    Robot.count), а serial — индивидуальным атрибутом экземпляра.

    Примеры:
        before = Robot.count
        r1 = Robot()
        r2 = Robot()
        Robot.count == before + 2
        r1.serial == before + 1
        r2.serial == before + 2
    """

    count = 0

    def __init__(self):
        Robot.count += 1
        self.serial = Robot.count


class Settings:
    """Задание 27. Динамические атрибуты.

    Конструктор принимает произвольные именованные параметры (**options)
    и сохраняет каждый как атрибут экземпляра. Метод get(key, default=None)
    возвращает значение атрибута по строковому имени или default, если
    атрибута нет (используйте getattr).

    Примеры:
        s = Settings(theme="dark", lang="ru")
        s.theme == "dark"
        s.lang == "ru"
        s.get("theme") == "dark"
        s.get("missing", 42) == 42
        s.get("missing") is None
    """

    def __init__(self, **options):
        for key, value in options.items():
            setattr(self, key, value)

    def get(self, key, default=None):
        return getattr(self, key, default)


class Point:
    """Задание 28. Точка: __repr__ и расстояние.

    Конструктор принимает координаты x и y. Метод distance_to(other) возвращает
    евклидово расстояние до другой точки (float). __repr__ возвращает строку
    "Point(x={x}, y={y})".

    Примеры:
        p = Point(1, 2)
        repr(p) == "Point(x=1, y=2)"
        Point(0, 0).distance_to(Point(3, 4)) == 5.0
        p.distance_to(p) == 0.0
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


class Money:
    """Задание 29. Сравнение через __eq__.

    Конструктор принимает сумму (amount) и валюту (currency).
    Две суммы равны (==), когда совпадают И сумма, И валюта.
    Сравнение с объектом другого типа возвращает False.

    Примеры:
        Money(100, "EUR") == Money(100, "EUR")      # True
        Money(100, "EUR") != Money(100, "USD")      # разные валюты
        Money(100, "EUR") != Money(150, "EUR")      # разные суммы
        Money(100, "EUR") == 100                    # False: не Money
    """

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency


class Vector:
    """Задание 30. Вектор: __add__, __mul__, magnitude().

    Конструктор принимает координаты x и y.
    __add__ возвращает НОВЫЙ Vector — покоординатную сумму.
    __mul__ принимает число-скаляр и возвращает новый Vector с умноженными
    координатами. magnitude() возвращает длину вектора (float).

    Примеры:
        v = Vector(1, 2) + Vector(3, 4)
        (v.x, v.y) == (4, 6)
        w = Vector(1, 2) * 3
        (w.x, w.y) == (3, 6)
        Vector(3, 4).magnitude() == 5.0
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
