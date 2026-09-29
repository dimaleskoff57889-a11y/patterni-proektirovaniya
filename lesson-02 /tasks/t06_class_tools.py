"""Тема 6. Инструменты класса: classmethod, staticmethod, property, магические методы."""


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
        raise NotImplementedError("Реализуйте MathUtils.is_even")

    @staticmethod
    def celsius_to_fahrenheit(c):
        raise NotImplementedError("Реализуйте MathUtils.celsius_to_fahrenheit")


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
        raise NotImplementedError("Реализуйте Date.__init__")

    @classmethod
    def from_string(cls, text):
        raise NotImplementedError("Реализуйте Date.from_string")


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
        raise NotImplementedError("Реализуйте Temperature.__init__")

    @property
    def fahrenheit(self):
        raise NotImplementedError("Реализуйте Temperature.fahrenheit")


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
        raise NotImplementedError("Реализуйте Account.__init__")

    @property
    def balance(self):
        raise NotImplementedError("Реализуйте геттер Account.balance")

    @balance.setter
    def balance(self, value):
        raise NotImplementedError("Реализуйте сеттер Account.balance")

    def deposit(self, amount):
        raise NotImplementedError("Реализуйте Account.deposit")


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
        raise NotImplementedError("Реализуйте Circle.__init__")

    @property
    def area(self):
        raise NotImplementedError("Реализуйте Circle.area")

    @property
    def perimeter(self):
        raise NotImplementedError("Реализуйте Circle.perimeter")


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
        raise NotImplementedError("Реализуйте Numbers.__init__")

    def add(self):
        raise NotImplementedError("Реализуйте Numbers.add")

    @classmethod
    def multiply(cls, a):
        raise NotImplementedError("Реализуйте Numbers.multiply")

    @staticmethod
    def subtract(b, c):
        raise NotImplementedError("Реализуйте Numbers.subtract")

    @property
    def value(self):
        raise NotImplementedError("Реализуйте Numbers.value")

    @value.setter
    def value(self, pair):
        raise NotImplementedError("Реализуйте сеттер Numbers.value")
