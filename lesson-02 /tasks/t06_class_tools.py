"""Тема 6. Инструменты класса: classmethod, staticmethod, property, магические методы."""

import math


class MathUtils:
    """Задание 31. Статические методы.

    Статический метод is_even(n) возвращает True для чётного целого числа.
    Статический метод celsius_to_fahrenheit(c) переводит градусы Цельсия
    в Фаренгейты по формуле c * 9 / 5 + 32. Оба метода объявлены через
    @staticmethod и не используют self/cls.

    Примеры:
        MathUtils.is_even(4) == True
        MathUtils.is_even(7) == False
        MathUtils.celsius_to_fahrenheit(0) == 32.0
        MathUtils.celsius_to_fahrenheit(100) == 212.0
        MathUtils().is_even(2) == True   # работает и через экземпляр
    """

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32


class Date:
    """Задание 32. Альтернативный конструктор.

    Конструктор принимает year, month, day (целые числа).
    Классовый метод from_string(text) разбирает строку "ГГГГ-ММ-ДД"
    и возвращает новый экземпляр Date с целочисленными полями.

    Примеры:
        d = Date(2024, 1, 15)
        (d.year, d.month, d.day) == (2024, 1, 15)
        d2 = Date.from_string("2023-12-31")
        isinstance(d2, Date)
        (d2.year, d2.month, d2.day) == (2023, 12, 31)
    """

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, text):
        year, month, day = text.split("-")
        return cls(int(year), int(month), int(day))


class Temperature:
    """Задание 33. Вычисляемое свойство.

    Конструктор принимает температуру в градусах Цельсия (атрибут celsius).
    Свойство fahrenheit вычисляется по формуле celsius * 9 / 5 + 32 и доступно
    только для чтения (попытка присваивания должна возбуждать AttributeError).

    Примеры:
        t = Temperature(0)
        t.celsius == 0
        t.fahrenheit == 32.0
        t.celsius = 100
        t.fahrenheit == 212.0
        t.fahrenheit = 0   # AttributeError
    """

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class Account:
    """Задание 34. Свойство с валидацией.

    Конструктор принимает владельца (owner) и начальный баланс (balance=0).
    Баланс доступен через свойство balance. Сеттер баланса отклоняет
    отрицательные значения: ValueError с сообщением, содержащим слово
    "отрицательным". Метод deposit(amount) пополняет баланс на amount.

    Примеры:
        acc = Account("Анна")
        acc.balance == 0
        acc.balance = 100
        acc.balance == 100
        acc.deposit(50)
        acc.balance == 150
        acc.balance = -1        # ValueError ... отрицательным ...
        acc.deposit(-5)         # ValueError
    """

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма пополнения не может быть отрицательным числом")
        self._balance += amount


class Circle:
    """Задание 35. Свойства только для чтения.

    Конструктор принимает радиус. Свойства area (площадь) и perimeter
    (длина окружности) вычисляются по радиусу и доступны только для чтения.
    Используйте math.pi.

    Примеры:
        c = Circle(1)
        c.area == math.pi       # приблизительно
        c.perimeter == 2 * math.pi
        c.radius = 2            # радиус менять можно
        c.area == 4 * math.pi
        c.area = 1              # AttributeError: площадь только для чтения
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class Numbers:
    """Задание 36. Numbers: сочетание всех инструментов класса.

    Атрибут класса MULTIPLIER = 3.5 общий для всех экземпляров.
    Конструктор принимает числа x и y.

    Методы:
      add()                     — сумма x и y;
      multiply(a)  (@classmethod)   — произведение a и MULTIPLIER;
      subtract(b, c) (@staticmethod) — разность b - c;
      value (@property)         — кортеж (x, y); имеет сеттер, который
                                  принимает кортеж из двух чисел и обновляет
                                  x и y.

    Примеры:
        n = Numbers(2, 3)
        n.add() == 5
        Numbers.multiply(4) == 14.0
        Numbers.subtract(10, 4) == 6
        n.value == (2, 3)
        n.value = (10, 20)
        n.value == (10, 20)
    """

    MULTIPLIER = 3.5

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, pair):
        self.x, self.y = pair
