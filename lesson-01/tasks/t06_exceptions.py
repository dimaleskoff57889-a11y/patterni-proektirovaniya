"""Тема 6. Ошибки и исключения: try/except, raise, with."""


def task_31(a, b):
    """Безопасное деление.

    Верните a / b. Если b равно нулю, перехватите ZeroDivisionError
    и верните None (исключение наружу пробрасывать нельзя).

    Примеры:
        task_31(7, 2) == 3.5
        task_31(9, 3) == 3.0
        task_31(1, 0) is None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def task_32(text):
    """Разбор целого числа из строки.

    Попытайтесь преобразовать text в int. Если строка не является целым
    числом, перехватите ValueError и верните None.

    Примеры:
        task_32("42") == 42
        task_32("-7") == -7
        task_32("4.2") is None
        task_32("abc") is None
    """
    try:
        return int(text)
    except ValueError:
        return None


def task_33(path):
    """Первая строка файла.

    Откройте файл по пути path (используйте конструкцию with) и верните его
    первую строку БЕЗ завершающего перевода строки. Если файла не существует,
    перехватите FileNotFoundError и верните пустую строку "". Если файл пуст — "".

    Примеры (файл со строками "привет\\nмир"):
        task_33(<путь>) == "привет"
        task_33(<несуществующий путь>) == ""
    """
    try:
        with open(path, encoding="utf-8") as f:
            return f.readline().rstrip("\n")
    except FileNotFoundError:
        return ""


def task_34(n):
    """Контроль значения через raise.

    Если n отрицательное, выбросьте исключение ValueError с сообщением,
    содержащим слово "неотрицательное". Иначе верните n.

    Примеры:
        task_34(5) == 5
        task_34(0) == 0
        with pytest.raises(ValueError, match="неотрицательное"):
            task_34(-1)
    """
    if n < 0:
        raise ValueError("n должно быть неотрицательное")
    return n


def task_35(items, index):
    """Элемент списка или сообщение об ошибке.

    Верните items[index]. Если индекс выходит за пределы списка, перехватите
    IndexError и верните строку "индекс вне диапазона".

    Примеры:
        task_35([10, 20, 30], 1) == 20
        task_35([10, 20, 30], -1) == 30     # отрицательные индексы допустимы
        task_35([10, 20, 30], 5) == "индекс вне диапазона"
        task_35([], 0) == "индекс вне диапазона"
    """
    try:
        return items[index]
    except IndexError:
        return "индекс вне диапазона"


def task_36(text):
    """Универсальный разбор числа.

    Верните значение text как число:
      - если строка — целое число, верните int;
      - если не целое, но число с плавающей точкой — верните float;
      - иначе верните None.
    Обрабатывайте исключения, а не проверяйте строку вручную.

    Примеры:
        task_36("7") == 7 and isinstance(task_36("7"), int)
        task_36("7.5") == 7.5 and isinstance(task_36("7.5"), float)
        task_36("abc") is None
    """
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        return None
