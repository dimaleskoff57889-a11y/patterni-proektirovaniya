"""Тесты к теме 2 «Переменные и область видимости» (задания 07–12)."""

import pytest

from tasks import t02_variables as v


@pytest.mark.parametrize("numbers, expected", [
    ([3, 1, 4, 1, 5], (1, 5)),
    ([7], (7, 7)),
    ([-2, -5, -1], (-5, -1)),
    ([0, 0], (0, 0)),
])
def test_task_07_min_max(numbers, expected):
    assert v.task_07(numbers) == expected


@pytest.mark.parametrize("total, expected", [
    (100, 120.0),
    (250.5, 300.6),
    (0, 0.0),
])
def test_task_08_price_with_tax(total, expected):
    assert v.task_08(total) == pytest.approx(expected)


def test_task_08_uses_tax_rate_constant(monkeypatch):
    # при изменении константы результат должен меняться соответственно
    monkeypatch.setattr(v, "TAX_RATE", 0.5)
    assert v.task_08(100) == pytest.approx(150.0)


@pytest.mark.parametrize("items, item, expected", [
    ([1, 2], 3, [1, 2, 3]),
    ([], "a", ["a"]),
])
def test_task_09_append_without_mutation(items, item, expected):
    original = list(items)
    assert v.task_09(items, item) == expected
    assert items == original  # исходный список не изменился


@pytest.mark.parametrize("values, expected", [
    (["1", "42", "-7"], [1, 42, -7]),
    ([], []),
    (["007"], [7]),
])
def test_task_10_parse_ints(values, expected):
    assert v.task_10(values) == expected


def test_task_11_multiplier_factory():
    assert v.task_11(3)(4) == 12
    assert v.task_11(0.5)(10) == 5.0
    f = v.task_11(7)
    assert f(2) == 14
    assert f(3) == 21


def test_task_12_mutate_dict_in_place():
    d = {"a": 1}
    result = v.task_12(d, "b", 2)
    assert result is d          # возвращён тот же объект
    assert d == {"a": 1, "b": 2}  # исходный словарь изменён
    v.task_12(d, "a", 99)
    assert d["a"] == 99
