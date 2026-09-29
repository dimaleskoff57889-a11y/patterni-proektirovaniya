"""Тесты к теме 5 «Операторы управления циклом» (задания 25–30)."""

import pytest

from tasks import t05_loops as lp


@pytest.mark.parametrize("n, expected", [
    (12345, 15),
    (0, 0),
    (999, 27),
    (1000000, 1),
])
def test_task_25_digit_sum(n, expected):
    assert lp.task_25(n) == expected


@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
])
def test_task_26_factorial(n, expected):
    assert lp.task_26(n) == expected


@pytest.mark.parametrize("n, expected", [
    (3, [[1, 2, 3], [2, 4, 6], [3, 6, 9]]),
    (1, [[1]]),
    (2, [[1, 2], [2, 4]]),
])
def test_task_27_multiplication_table(n, expected):
    assert lp.task_27(n) == expected


def test_task_28_zip_to_dict():
    assert lp.task_28(["январь", "февраль"], [31, 28]) == {"январь": 31, "февраль": 28}
    assert lp.task_28([], []) == {}


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], [4, 16]),
    ([1, 3], []),
    ([], []),
    ([2, 2], [4, 4]),
])
def test_task_29_squares_of_evens(numbers, expected):
    assert lp.task_29(numbers) == expected


@pytest.mark.parametrize("numbers, stop, expected", [
    ([5, 7, -1, 9], -1, 12),
    ([1, 2], 99, 3),
    ([0, 1, 2], 0, 0),
    ([1, 2, 3, 2], 2, 1),
])
def test_task_30_sum_until_sentinel(numbers, stop, expected):
    assert lp.task_30(numbers, stop) == expected
