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
        self.name = name
        self.age = age
        self.role = role

    @classmethod
    def from_string(cls, text):
        name, age, role = text.split(";")
        return cls(name, int(age), role)

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
        self._password = raw

    @property
    def password(self):
        return "*" * len(self._password)

    @property
    def is_strong(self):
        has_length = len(self._password) >= 8
        has_upper = any(c.isupper() for c in self._password)
        has_digit = any(c.isdigit() for c in self._password)
        return has_length and has_upper and has_digit

    def check(self, candidate):
        return self._password == candidate


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
        self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def mean(self):
        if not self.values:
            return None
        return sum(self.values) / len(self.values)
