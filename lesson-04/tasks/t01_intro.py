"""Тема 1. Введение: каталог GoF, мотивация, словарь."""

GROUPS = {
    "порождающие": [
        "Singleton", "Factory Method", "Abstract Factory", "Builder", "Prototype",
    ],
    "структурные": [
        "Adapter", "Bridge", "Composite", "Decorator", "Facade", "Flyweight", "Proxy",
    ],
    "поведенческие": [
        "Chain of Responsibility", "Command", "Interpreter", "Iterator", "Mediator",
        "Memento", "Observer", "State", "Strategy", "Template Method", "Visitor",
    ],
}


def task_01(name):
    """Группа паттерна.

    Верните название группы каталога GoF для паттерна name:
    "порождающие", "структурные" или "поведенческие".
    Для неизвестного имени верните None. Используйте словарь GROUPS выше,
    а не лестницу if/elif.

    Примеры:
        task_01("Singleton") == "порождающие"
        task_01("Adapter") == "структурные"
        task_01("Observer") == "поведенческие"
        task_01("Visitor") == "поведенческие"
        task_01("MVC") is None
    """
    for group, patterns in GROUPS.items():
        if name in patterns:
            return group
    return None


def task_02():
    """Размеры групп каталога.

    Верните словарь вида {"порождающие": 5, "структурные": 7, "поведенческие": 11}.
    Посчитайте размеры из GROUPS, а не пишите числа вручную.

    Примеры:
        task_02() == {"порождающие": 5, "структурные": 7, "поведенческие": 11}
    """
    return {group: len(patterns) for group, patterns in GROUPS.items()}


def task_03(text):
    """Паттерн по формулировке намерения.

    Верните имя паттерна, которому соответствует формулировка. Известные
    формулировки (в text входит ровно одна):
      "единственный экземпляр"            → "Singleton"
      "семейство связанных объектов"      → "Abstract Factory"
      "пошаговая сборка сложного объекта" → "Builder"
      "копирование готового образца"      → "Prototype"
      "адаптация чужого интерфейса"       → "Adapter"
      "уведомление подписчиков"           → "Observer"
    Если ни одна не входит — None.

    Примеры:
        task_03("нужен единственный экземпляр на всё приложение") == "Singleton"
        task_03("хочу уведомление подписчиков об изменениях") == "Observer"
        task_03("просто перебрать список") is None
    """
    intents = {
        "единственный экземпляр": "Singleton",
        "семейство связанных объектов": "Abstract Factory",
        "пошаговая сборка сложного объекта": "Builder",
        "копирование готового образца": "Prototype",
        "адаптация чужого интерфейса": "Adapter",
        "уведомление подписчиков": "Observer",
    }
    for phrase, pattern in intents.items():
        if phrase in text:
            return pattern
    return None


class Clicker:
    """Задание 04. Состояние в объекте — зачем нам классы.

    Метод click() увеличивает внутренний счётчик; count() возвращает его
    значение; reset() обнуляет. Два щелкателя независимы.

    Примеры:
        c = Clicker()
        c.count() == 0
        c.click(); c.click()
        c.count() == 2
        c.reset()
        c.count() == 0
        other = Clicker(); other.click()
        other.count() == 1
    """

    def __init__(self):
        self._count = 0

    def click(self):
        self._count += 1

    def count(self):
        return self._count

    def reset(self):
        self._count = 0


def task_05(method):
    """Диспетчеризация словарём.

    HTTP-роутер без лестницы if/elif: верните "{method}: обработан" для методов
    "get", "post", "put" и "delete"; для остальных — "неизвестный метод".
    Используйте словарь.

    Примеры:
        task_05("get") == "get: обработан"
        task_05("delete") == "delete: обработан"
        task_05("patch") == "неизвестный метод"
    """
    handled = {"get", "post", "put", "delete"}
    return f"{method}: обработан" if method in handled else "неизвестный метод"


class AppConfig:
    """Задание 06. Два независимых экземпляра — контраст к Singleton.

    set(key, value) сохраняет настройку; get(key, default=None) читает;
    keys() возвращает отсортированный список ключей. Каждый экземпляр
    хранит СВОИ настройки (в следующей теме мы сделаем противоположное).

    Примеры:
        a = AppConfig()
        a.set("тема", "тёмная")
        a.get("тема") == "тёмная"
        b = AppConfig()
        b.get("тема") is None          # у b своих настроек нет
        a.keys() == ["тема"]
    """

    def __init__(self):
        self._settings = {}

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key, default=None):
        return self._settings.get(key, default)

    def keys(self):
        return sorted(self._settings)
