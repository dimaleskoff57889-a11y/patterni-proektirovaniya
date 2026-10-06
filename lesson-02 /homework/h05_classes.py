"""Домашнее задание. Тема 5: классы."""


class Stack:
    """Задание 15. Стек (LIFO).

    Методы:
      push(item)  — положить элемент на вершину;
      pop()       — снять и вернуть элемент с вершины; для пустого стека
                    возбуждает IndexError;
      peek()      — вернуть вершину без снятия; для пустого — IndexError;
      is_empty()  — True, если стек пуст.

    Примеры:
        s = Stack()
        s.is_empty() == True
        s.push(1)
        s.push(2)
        s.is_empty() == False
        s.peek() == 2
        s.pop() == 2
        s.pop() == 1
        s.pop()  # IndexError
    """

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0


class Queue:
    """Задание 16. Очередь (FIFO).

    Методы:
      enqueue(item) — добавить элемент в конец очереди;
      dequeue()     — извлечь и вернуть элемент из начала; для пустой очереди
                      возбуждает IndexError;
      size()        — текущее число элементов (int).

    Примеры:
        q = Queue()
        q.size() == 0
        q.enqueue("первый")
        q.enqueue("второй")
        q.size() == 2
        q.dequeue() == "первый"
        q.dequeue() == "второй"
        q.dequeue()  # IndexError
    """

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.size() == 0:
            raise IndexError("Очередь пуста")
        return self._items.pop(0)

    def size(self):
        return len(self._items)


class Book:
    """Задание 17, часть 1. Книга.

    Конструктор принимает title и author и сохраняет их как атрибуты.

    Примеры:
        b = Book("Мёртвые души", "Гоголь")
        b.title == "Мёртвые души"
        b.author == "Гоголь"
    """

    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    """Задание 17, часть 2. Библиотека (хранит книги — композиция).

    Методы:
      add(book)           — добавить книгу;
      titles()            — список названий в порядке добавления;
      by_author(author)   — список названий книг заданного автора
                            (в порядке добавления).

    Примеры:
        lib = Library()
        lib.add(Book("Мёртвые души", "Гоголь"))
        lib.add(Book("Ревизор", "Гоголь"))
        lib.add(Book("Евгений Онегин", "Пушкин"))
        lib.titles() == ["Мёртвые души", "Ревизор", "Евгений Онегин"]
        lib.by_author("Гоголь") == ["Мёртвые души", "Ревизор"]
        lib.by_author("Толстой") == []
    """

    def __init__(self):
        self._books = []

    def add(self, book):
        self._books.append(book)

    def titles(self):
        return [book.title for book in self._books]

    def by_author(self, author):
        return [book.title for book in self._books if book.author == author]
