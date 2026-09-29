"""Домашнее задание. Тема 6: инструменты класса."""


class Employee:
    """Задание 18. Альтернативный конструктор.

    Конструктор принимает name (str), age (int), role (str).
    Классовый метод from_string(text) разбирает строку "имя;возраст;должность"
    и возвращает экземпляр Employee (возраст — int).

    Примеры:
        e = Employee("Иван", 30, "разработчик")
        (e.name, e.age, e.role) == ("Иван", 30, "разработчик")
        e2 = Employee.from_string("Ольга;25;тестировщик")
        isinstance(e2, Employee)
        (e2.name, e2.age, e2.role) == ("Ольга", 25, "тестировщик")
    """

    def __init__(self, name, age, role):
        raise NotImplementedError("Реализуйте Employee.__init__")

    @classmethod
    def from_string(cls, text):
        raise NotImplementedError("Реализуйте Employee.from_string")


class Password:
    """Задание 19. Свойство-маска и проверка надёжности.

    Конструктор принимает исходный пароль и хранит его «про себя»
    (например, в _password). Свойство password возвращает строку из
    звёздочек той же длины и доступно только для чтения (присваивание —
    AttributeError). Свойство is_strong: True, если длина пароля >= 8,
    есть заглавная буква и цифра. Метод check(candidate) сравнивает
    candidate с исходным паролем (True/False).

    Примеры:
        p = Password("Str0ngPass")
        p.password == "**********"
        p.is_strong == True
        p.check("Str0ngPass") == True
        p.check("wrong") == False
        weak = Password("abc")
        weak.is_strong == False
        p.password = "x"   # AttributeError
    """

    def __init__(self, raw):
        raise NotImplementedError("Реализуйте Password.__init__")

    @property
    def password(self):
        raise NotImplementedError("Реализуйте Password.password")

    @property
    def is_strong(self):
        raise NotImplementedError("Реализуйте Password.is_strong")

    def check(self, candidate):
        raise NotImplementedError("Реализуйте Password.check")


class Stats:
    """Задание 20. Магические методы len и индексирование.

    Конструктор принимает список чисел values.
    __len__ возвращает количество значений; __getitem__(index) возвращает
    значение по индексу (срезы тоже должны работать как у списка);
    mean() возвращает среднее (float) или None для пустого набора.

    Примеры:
        s = Stats([2, 4, 6, 8])
        len(s) == 4
        s[0] == 2
        s[-1] == 8
        s[1:3] == [4, 6]
        s.mean() == 5.0
        len(Stats([])) == 0
        Stats([]).mean() is None
    """

    def __init__(self, values):
        raise NotImplementedError("Реализуйте Stats.__init__")

    def __len__(self):
        raise NotImplementedError("Реализуйте Stats.__len__")

    def __getitem__(self, index):
        raise NotImplementedError("Реализуйте Stats.__getitem__")

    def mean(self):
        raise NotImplementedError("Реализуйте Stats.mean")
