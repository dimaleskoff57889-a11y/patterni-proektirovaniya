"""Тесты к теме 1 «Основы Python» (задания 01–06)."""

import pytest

from tasks import t01_basics as b


@pytest.mark.parametrize("a, b_, c, expected", [
    (1, 2, 3, 2.0),
    (10, 20, 40, 70 / 3),
    (-1, 0, 1, 0.0),
])
def test_task_01_mean(a, b_, c, expected):
    assert b.task_01(a, b_, c) == pytest.approx(expected)
    assert isinstance(b.task_01(1, 2, 3), float)


@pytest.mark.parametrize("seconds, expected", [
    (3661, (1, 1, 1)),
    (59, (0, 0, 59)),
    (0, (0, 0, 0)),
    (3600, (1, 0, 0)),
    (60, (0, 1, 0)),
])
def test_task_02_split_seconds(seconds, expected):
    assert b.task_02(seconds) == expected


@pytest.mark.parametrize("fahrenheit, celsius", [
    (212, 100.0),
    (32, 0.0),
    (98.6, 37.0),
    (-40, -40.0),
])
def test_task_03_fahrenheit_to_celsius(fahrenheit, celsius):
    assert b.task_03(fahrenheit) == pytest.approx(celsius)


@pytest.mark.parametrize("price, discount, expected", [
    (1000, 25, 750.0),
    (199.99, 10, 179.99),
    (500, 0, 500.0),
    (100, 100, 0.0),
])
def test_task_04_price_with_discount(price, discount, expected):
    assert b.task_04(price, discount) == pytest.approx(expected)


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, "2 + 3 = 5"),
    (-1, 1, "-1 + 1 = 0"),
    (1.5, 2, "1.5 + 2 = 3.5"),
])
def test_task_05_sum_report(x, y, expected):
    assert b.task_05(x, y) == expected


@pytest.mark.parametrize("name, expected", [
    ("  аННА   пЕТРОВА  ", "Анна Петрова"),
    ("иван", "Иван"),
    ("  ЖАН-КЛОД  ван дАММ ", "Жан-клод Ван Дамм"),
])
def test_task_06_normalize_name(name, expected):
    assert b.task_06(name) == expected
