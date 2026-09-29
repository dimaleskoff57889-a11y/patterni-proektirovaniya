"""Тесты к теме 4 «Коллекции» (задания 19–24)."""

import pytest

from tasks import t04_collections as col


@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 2], [3, 2, 1]),
    ([5], [5]),
    ([1, 2, 3], [3, 2, 1]),
])
def test_task_19_sorted_desc_copy(numbers, expected):
    original = list(numbers)
    assert col.task_19(numbers) == expected
    assert numbers == original  # оригинал не изменился


@pytest.mark.parametrize("items, expected", [
    ((1, 2, 3, 4, 5), (2, 3, 4)),
    ((1, 2), ()),
    ((5,), ()),
    ((), ()),
])
def test_task_20_tuple_without_edges(items, expected):
    assert col.task_20(items) == expected


def test_task_21_set_operations():
    assert col.task_21({1, 2, 3}, {3, 4}) == {
        "union": [1, 2, 3, 4],
        "intersection": [3],
        "a_minus_b": [1, 2],
    }
    assert col.task_21(set(), {1}) == {
        "union": [1],
        "intersection": [],
        "a_minus_b": [],
    }


@pytest.mark.parametrize("text, expected", [
    ("кот кот пёс", {"кот": 2, "пёс": 1}),
    ("раз два три раз два раз", {"раз": 3, "два": 2, "три": 1}),
    ("", {}),
    ("одно  слово   с  пробелами", {"одно": 1, "слово": 1, "с": 1, "пробелами": 1}),
])
def test_task_22_word_frequencies(text, expected):
    assert col.task_22(text) == expected


@pytest.mark.parametrize("text, expected", [
    ("А роза упала на лапу Азора", True),
    ("Аргентина манит негра", True),
    ("привет", False),
    ("", True),
    ("1 2 3 2 1", True),
])
def test_task_23_palindrome(text, expected):
    assert col.task_23(text) is expected


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2], [3, 4]], 5),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),
    ([[10]], 10),
])
def test_task_24_diagonal_sum(matrix, expected):
    assert col.task_24(matrix) == expected
