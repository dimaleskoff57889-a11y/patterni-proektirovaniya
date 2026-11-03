"""Тема 5. Порождающие вместе: синглтон + фабрика, ленивые реестры."""


class Logger:
    """Задание 25, часть 1. Логгер с журналом messages (список).

    log(message) добавляет сообщение в журнал.
    """

    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)


def task_25():
    """Задание 25, часть 2. Синглтон-логгер через функцию.

    Каждый вызов task_25() возвращает ОДИН И ТОТ ЖЕ объект Logger
    (храните его в атрибуте функции или в замыкании модуля — без глобальных
    переменных через global).

    Примеры:
        task_25() is task_25()
        task_25().log("старт")
        task_25().messages == ["старт"]   # журнал общий
    """
    if not hasattr(task_25, "_logger"):
        task_25._logger = Logger()
    return task_25._logger


class Pool:
    """Задание 26. Синглтон-пул соединений.

    Пул соединений: acquire() возвращает свободное соединение (строку
    "conn-1", "conn-2", ...); если свободных нет — создаёт новое с очередным
    номером. release(conn) возвращает соединение в пул, и следующий acquire
    переиспользует его. Пул один на всё приложение.

    Примеры:
        Pool() is Pool()
        p = Pool()
        first = p.acquire()      # "conn-1"
        second = p.acquire()     # "conn-2"
        p.release(first)
        p.acquire() == "conn-1"  # переиспользовали
    """

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance._free = []
            cls._instance._created = 0
        return cls._instance

    def acquire(self):
        if self._free:
            return self._free.pop(0)
        self._created += 1
        return f"conn-{self._created}"

    def release(self, conn):
        self._free.append(conn)


def task_27(func):
    """Задание 27. Фабрика кэширующих обёрток.

    Верните функцию, которая вызывает func только при ПЕРВОМ обращении
    с данным аргументом и кэширует результат. У обёртки должен быть атрибут
    cache — словарь {аргументы-кортежем: результат}.

    Примеры:
        calls = []
        def slow(x):
            calls.append(x)
            return x * x

        fast = task_27(slow)
        fast(2) == 4
        fast(2) == 4
        calls == [2]              # второй раз не считали
        fast.cache == {(2,): 4}
    """
    def wrapper(*args):
        if args not in wrapper.cache:
            wrapper.cache[args] = func(*args)
        return wrapper.cache[args]

    wrapper.cache = {}
    return wrapper


class AppConfig:
    """Задание 28. AppConfig становится синглтоном.

    Сделайте то же, что в задании 06 темы 1 (set/get/keys), но теперь
    все вызовы AppConfig() возвращают один объект: настройки общие
    для всего приложения. Не забудьте защиту от повторного __init__.

    Примеры:
        AppConfig() is AppConfig()
        a = AppConfig()
        a.set("тема", "тёмная")
        AppConfig().get("тема") == "тёмная"
        AppConfig().keys() == ["тема"]
    """

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def keys(self):
        return sorted(self._settings)


class Registry:
    """Задание 29. Ленивые синглтоны по ключу.

    register(name, factory) запоминает фабрику (функцию без аргументов).
    get(name): при первом вызове создаёт объект фабрикой и кэширует;
    повторные вызовы возвращают ТОТ ЖЕ объект. Неизвестное имя — KeyError.

    Примеры:
        r = Registry()
        r.register("logger", lambda: Logger())
        a = r.get("logger")
        b = r.get("logger")
        a is b
        r.get("нет")  # KeyError
    """

    def __init__(self):
        self._factories = {}
        self._instances = {}

    def register(self, name, factory):
        self._factories[name] = factory

    def get(self, name):
        if name not in self._instances:
            self._instances[name] = self._factories[name]()
        return self._instances[name]


class SimpleTask:
    """Продукт для задания 30."""

    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"задача {self.name}: простая"


class DelayedTask:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"задача {self.name}: отложенная"


class TaskFactory:
    """Задание 30, часть 1. Фабрика задач.

    create(kind, name): "simple" → SimpleTask(name), "delayed" → DelayedTask(name).
    Неизвестный kind — ValueError("неизвестный тип задачи").
    """

    @staticmethod
    def create(kind, name):
        tasks = {"simple": SimpleTask, "delayed": DelayedTask}
        if kind not in tasks:
            raise ValueError("неизвестный тип задачи")
        return tasks[kind](name)


class Scheduler:
    """Задание 30, часть 2. Капстоун: синглтон-планировщик.

    Планировщик — синглтон. add(task) добавляет задачу в очередь;
    run_all() выполняет все задачи и возвращает список их describe(),
    ОЧИЩАЯ очередь.

    Примеры:
        Scheduler() is Scheduler()
        s = Scheduler()
        s.add(TaskFactory.create("simple", "купить хлеб"))
        s.add(TaskFactory.create("delayed", "позвонить маме"))
        s.run_all() == ["задача купить хлеб: простая",
                        "задача позвонить маме: отложенная"]
        s.run_all() == []        # очередь очищена
    """

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance._queue = []
        return cls._instance

    def add(self, task):
        self._queue.append(task)

    def run_all(self):
        results = [task.describe() for task in self._queue]
        self._queue.clear()
        return results
