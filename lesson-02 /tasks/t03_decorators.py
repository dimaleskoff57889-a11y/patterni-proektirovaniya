"""Тема 3. Замыкания и декораторы."""

from decimal import Decimal
from functools import wraps
from itertools import chain
from numbers import Real


def task_13(start=0):
    """Счётчик вызовов на замыкании.

    Верните функцию без аргументов, которая при каждом вызове возвращает
    следующее целое число: start + 1, start + 2, ... Состояние храните
    в замыкании (nonlocal), без глобальных переменных.

    Примеры:
        c = task_13()
        c() == 1; c() == 2; c() == 3
        c10 = task_13(10)
        c10() == 11; c10() == 12
    """
    def counter():
        nonlocal start
        start += 1
        return start

    return counter


def task_14(func):
    """Декоратор count_calls.

    Напишите декоратор, который считает вызовы функции. Обёртка должна иметь
    атрибут calls (int), равный нулю сразу после декорирования и увеличивающийся
    на 1 перед каждым вызовом. Результат декорируемой функции пробрасывается.

    Примеры:
        @task_14
        def double(x): return x * 2

        double.calls == 0
        double(2) == 4
        double.calls == 1
        double(3) == 6
        double.calls == 2
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def task_15(func):
    """Декоратор uppercase_result.

    Декоратор возвращает обёртку, которая приводит строковый результат вызова
    func к верхнему регистру. Нестроковый результат возвращается без изменений.

    Примеры:
        @task_15
        def greet(name): return f"привет, {name}"

        greet("анна") == "ПРИВЕТ, АННА"

        @task_15
        def add(a, b): return a + b

        add(1, 2) == 3
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result

    return wrapper


def task_16(func):
    """Декоратор memoize.

    Декоратор кэширует результаты вызовов func по позиционным аргументам.
    Повторный вызов с теми же аргументами не должен вызывать исходную функцию.
    Для простоты считайте, что func вызывается только с позиционными аргументами.

    Примеры:
        calls = []
        def slow_square(x):
            calls.append(x)
            return x * x

        fast = task_16(slow_square)
        fast(2) == 4
        fast(2) == 4
        calls == [2]          # второй раз исходная функция не вызывалась
        fast(3) == 9
        calls == [2, 3]
    """
    cache = []

    @wraps(func)
    def wrapper(*args):
        for cached_args, result in cache:
            if args == cached_args:
                return result

        result = func(*args)
        cache.append((args, result))
        return result

    return wrapper


def task_17(func):
    """Декоратор require_positive.

    Декоратор проверяет аргументы вызова: если хотя бы один позиционный
    или именованный аргумент — число меньше нуля, выбросьте ValueError
    с сообщением, содержащим слово "неотрицательными". Иначе верните
    результат func.

    Примеры:
        @task_17
        def sub(a, b): return a - b

        sub(10, 4) == 6
        sub(10, -4)  # ValueError ... неотрицательными ...
        sub(a=1, b=-2)  # ValueError
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in chain(args, kwargs.values()):
            if isinstance(value, (Real, Decimal)) and value < 0:
                raise ValueError("Аргументы должны быть неотрицательными")
        return func(*args, **kwargs)

    return wrapper


def task_18(times):
    """Фабрика декораторов repeat.

    task_18(n) возвращает декоратор, при применении которого вызов функции
    выполняется n раз, а обёртка возвращает СПИСОК всех результатов.
    Для n == 0 — пустой список (функция не вызывается ни разу).

    Примеры:
        @task_18(3)
        def inc(x): return x + 1

        inc(1) == [2, 2, 2]

        @task_18(0)
        def nothing(): return "x"

        nothing() == []
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]

        return wrapper

    return decorator
