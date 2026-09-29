"""Тема 3. Операторы ветвления: if/elif/else, логические операторы, словарь вместо switch."""


def task_13(n):
    """Знак числа.

    Верните 1, если n положительное; -1, если отрицательное; 0, если ноль.

    Примеры:
        task_13(42) == 1
        task_13(-3) == -1
        task_13(0) == 0
    """
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def task_14(score):
    """Оценка по баллам.

    Верните строку с оценкой по 100-балльной шкале:
      90 и выше     — "отлично"
      75–89         — "хорошо"
      60–74         — "удовлетворительно"
      ниже 60       — "неудовлетворительно"

    Примеры:
        task_14(90) == "отлично"
        task_14(89) == "хорошо"
        task_14(60) == "удовлетворительно"
        task_14(59) == "неудовлетворительно"
    """
    if score >= 90:
        return "отлично"
    if score >= 75:
        return "хорошо"
    if score >= 60:
        return "удовлетворительно"
    return "неудовлетворительно"


def task_15(age, is_citizen):
    """Право голоса.

    Человек может голосовать, если ему 18 лет или больше И он является
    гражданином. Верните True или False.

    Примеры:
        task_15(19, True) == True
        task_15(19, False) == False
        task_15(17, True) == False
        task_15(18, True) == True
    """
    return age >= 18 and is_citizen


def task_16(password):
    """Валидный пароль.

    Пароль валиден, если одновременно:
      - его длина не меньше 8 символов;
      - есть хотя бы одна заглавная буква;
      - есть хотя бы одна цифра.
    Верните True или False.

    Примеры:
        task_16("Str0ngPass") == True
        task_16("str0ngpass") == False   # нет заглавной
        task_16("StrongPass") == False   # нет цифры
        task_16("Str1") == False         # короткий
    """
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    return len(password) >= 8 and has_upper and has_digit


def task_17(year):
    """Високосный год.

    Год високосный, если он делится на 4, но не делится на 100,
    либо делится на 400. Верните True или False.

    Примеры:
        task_17(2024) == True
        task_17(2023) == False
        task_17(1900) == False   # делится на 100, но не на 400
        task_17(2000) == True    # делится на 400
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def task_18(op, a, b):
    """Калькулятор через словарь операций.

    Реализуйте калькулятор, выбирающий операцию по строке op.
    Поддерживаются "+", "-", "*", "/". Верните результат операции.
    Для неизвестной операции и для деления на ноль верните None.
    Рекомендуемый способ — словарь {операция: функция} вместо длинной
    лестницы if/elif (в Python так часто заменяют switch).

    Примеры:
        task_18("+", 2, 3) == 5
        task_18("*", 4, 2.5) == 10.0
        task_18("/", 7, 2) == 3.5
        task_18("/", 5, 0) is None
        task_18("^", 2, 3) is None
    """
    if op == "/" and b == 0:
        return None
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    func = operations.get(op)
    if func is None:
        return None
    return func(a, b)
