"""Тема 4. Abstract Factory: семейства продуктов."""


class Button:
    """Продукт-кнопка со стилем style."""

    def __init__(self, style):
        self.style = style

    def render(self):
        return f"{self.style} кнопка"


class Checkbox:
    def __init__(self, style):
        self.style = style

    def render(self):
        return f"{self.style} галочка"


class LightFactory:
    """Задание 19, часть 1. Фабрика светлой темы.

    create_button() → Button("светлая"); create_checkbox() → Checkbox("светлая").

    Примеры:
        LightFactory().create_button().render() == "светлая кнопка"
        LightFactory().create_checkbox().render() == "светлая галочка"
    """

    def create_button(self):
        return Button("светлая")

    def create_checkbox(self):
        return Checkbox("светлая")


class DarkFactory:
    """Задание 19, часть 2. Фабрика тёмной темы: продукты со стилем "тёмная".

    Примеры:
        DarkFactory().create_button().render() == "тёмная кнопка"
        DarkFactory().create_checkbox().render() == "тёмная галочка"
    """

    def create_button(self):
        return Button("тёмная")

    def create_checkbox(self):
        return Checkbox("тёмная")


def task_20(factory):
    """Задание 20. Клиентский код.

    Верните список [кнопка.render(), галочка.render()], взяв продукты
    у переданной фабрики. Функция не знает, какая это тема, — работает
    с ЛЮБОЙ фабрикой, у которой есть create_button и create_checkbox.

    Примеры:
        task_20(LightFactory()) == ["светлая кнопка", "светлая галочка"]
        task_20(DarkFactory()) == ["тёмная кнопка", "тёмная галочка"]
    """
    return [factory.create_button().render(), factory.create_checkbox().render()]


def task_21(theme):
    """Задание 21. Фабрика фабрик.

    Верните фабрику по теме: "light" → LightFactory, "dark" → DarkFactory.
    Неизвестная тема — ValueError("неизвестная тема").

    Примеры:
        isinstance(task_21("light"), LightFactory)
        task_21("dark").create_button().render() == "тёмная кнопка"
        task_21("retro")  # ValueError: неизвестная тема
    """
    factories = {"light": LightFactory, "dark": DarkFactory}
    if theme not in factories:
        raise ValueError("неизвестная тема")
    return factories[theme]()


class Chair:
    """Продукт: стул стиля style."""

    def __init__(self, style):
        self.style = style

    def sit(self):
        return f"{self.style} стул"


class Sofa:
    def __init__(self, style):
        self.style = style

    def lie(self):
        return f"{self.style} диван"


class ModernFactory:
    """Задание 22, часть 1. Мебельная фабрика: стиль "современный".

    create_chair() → Chair("современный"); create_sofa() → Sofa("современный").

    Примеры:
        ModernFactory().create_chair().sit() == "современный стул"
        ModernFactory().create_sofa().lie() == "современный диван"
    """

    def create_chair(self):
        return Chair("современный")

    def create_sofa(self):
        return Sofa("современный")


class ClassicFactory:
    """Задание 22, часть 2. Мебельная фабрика: стиль "классический".

    Примеры:
        ClassicFactory().create_chair().sit() == "классический стул"
        ClassicFactory().create_sofa().lie() == "классический диван"
    """

    def create_chair(self):
        return Chair("классический")

    def create_sofa(self):
        return Sofa("классический")


class TaggedButton:
    """Задание 23, часть 1. Кнопка с ярлыком семейства family."""

    def __init__(self, family):
        self.family = family


def task_23(items):
    """Задание 23, часть 2. Согласованность семейства.

    Верните True, если у ВСЕХ объектов из items атрибут family одинаковый
    (пустой список считается согласованным), иначе False. Абстрактная фабрика
    гарантирует такую согласованность по построению — здесь проверяем её явно.

    Примеры:
        task_23([TaggedButton("light"), TaggedButton("light")]) == True
        task_23([TaggedButton("light"), TaggedButton("dark")]) == False
        task_23([]) == True
    """
    return len({item.family for item in items}) <= 1


def task_24(theme):
    """Задание 24. Капстоун: диалог на любой теме.

    Используя task_21 (выбор фабрики) и task_20 (клиентский код), верните
    список отрендеренных элементов диалога для темы theme. Неизвестная
    тема — ValueError.

    Примеры:
        task_24("light") == ["светлая кнопка", "светлая галочка"]
        task_24("dark") == ["тёмная кнопка", "тёмная галочка"]
    """
    return task_20(task_21(theme))
