"""Тесты к теме 3 «Операторы ветвления» (задания 13–18)."""

import pytest

from tasks import t03_branching as br


@pytest.mark.parametrize("n, expected", [
    (42, 1),
    (-3, -1),
    (0, 0),
    (0.0, 0),
])
def test_task_13_sign(n, expected):
    assert br.task_13(n) == expected


@pytest.mark.parametrize("score, expected", [
    (100, "отлично"),
    (90, "отлично"),
    (89, "хорошо"),
    (75, "хорошо"),
    (74, "удовлетворительно"),
    (60, "удовлетворительно"),
    (59, "неудовлетворительно"),
    (0, "неудовлетворительно"),
])
def test_task_14_grade(score, expected):
    assert br.task_14(score) == expected


@pytest.mark.parametrize("age, is_citizen, expected", [
    (19, True, True),
    (19, False, False),
    (17, True, False),
    (18, True, True),
    (100, True, True),
])
def test_task_15_can_vote(age, is_citizen, expected):
    assert br.task_15(age, is_citizen) is expected


@pytest.mark.parametrize("password, expected", [
    ("Str0ngPass", True),
    ("str0ngpass", False),
    ("StrongPass", False),
    ("Str1", False),
    ("12345678", False),
    ("Abcdefg1", True),
])
def test_task_16_valid_password(password, expected):
    assert br.task_16(password) is expected


@pytest.mark.parametrize("year, expected", [
    (2024, True),
    (2023, False),
    (1900, False),
    (2000, True),
    (1996, True),
])
def test_task_17_leap_year(year, expected):
    assert br.task_17(year) is expected


@pytest.mark.parametrize("op, a, b_, expected", [
    ("+", 2, 3, 5),
    ("-", 10, 4, 6),
    ("*", 4, 2.5, 10.0),
    ("/", 7, 2, 3.5),
])
def test_task_18_calculator(op, a, b_, expected):
    assert br.task_18(op, a, b_) == pytest.approx(expected)


@pytest.mark.parametrize("op, a, b_", [
    ("/", 5, 0),
    ("^", 2, 3),
    ("", 1, 1),
])
def test_task_18_calculator_returns_none(op, a, b_):
    assert br.task_18(op, a, b_) is None
