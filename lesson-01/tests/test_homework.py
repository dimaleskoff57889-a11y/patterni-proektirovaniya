"""Тесты к домашнему заданию (задания 01–20)."""

import pytest

from homework import h01_basics as hb1
from homework import h02_variables as hb2
from homework import h03_branching as hb3
from homework import h04_collections as hb4
from homework import h05_loops as hb5
from homework import h06_exceptions as hb6


@pytest.mark.parametrize("seconds, expected", [
    (3661, "01:01:01"),
    (59, "00:00:59"),
    (0, "00:00:00"),
    (3600, "01:00:00"),
    (86399, "23:59:59"),
])
def test_hw_01_seconds_to_hms(seconds, expected):
    assert hb1.hw_01(seconds) == expected


@pytest.mark.parametrize("a, b_, c, expected", [
    (3, 4, 5, 6.0),
    (5, 5, 6, 12.0),
    (1, 1, 1.4142135623730951, 0.5),
])
def test_hw_02_heron_area(a, b_, c, expected):
    assert hb1.hw_02(a, b_, c) == pytest.approx(expected)


@pytest.mark.parametrize("card, expected", [
    ("1234567812345678", "************5678"),
    ("1234", "1234"),
    ("987210", "**7210"),
])
def test_hw_03_mask_card(card, expected):
    assert hb1.hw_03(card) == expected


@pytest.mark.parametrize("x, y, expected", [
    (7, 3, "7 / 3 = 2.33"),
    (10, 4, "10 / 4 = 2.50"),
    (1, 2, "1 / 2 = 0.50"),
])
def test_hw_04_division_report(x, y, expected):
    assert hb1.hw_04(x, y) == expected


def test_hw_05_accumulator():
    acc = hb2.hw_05()
    assert acc(5) == 5
    assert acc(3) == 8
    assert acc(0) == 8
    assert acc(-10) == -2


def test_hw_05_accumulators_are_independent():
    first = hb2.hw_05()
    second = hb2.hw_05()
    first(100)
    assert second(1) == 1  # у каждого замыкания своё состояние


def test_hw_06_merge_settings():
    defaults = {"тема": "светлая", "язык": "ru"}
    settings = {"тема": "тёмная"}
    result = hb2.hw_06(settings, defaults)
    assert result == {"тема": "тёмная", "язык": "ru"}
    assert defaults == {"тема": "светлая", "язык": "ru"}  # не изменились
    assert settings == {"тема": "тёмная"}                 # не изменились


@pytest.mark.parametrize("month, expected", [
    (12, "зима"), (1, "зима"), (2, "зима"),
    (3, "весна"), (5, "весна"),
    (6, "лето"), (8, "лето"),
    (9, "осень"), (11, "осень"),
    (0, None), (13, None),
])
def test_hw_07_season(month, expected):
    assert hb3.hw_07(month) == expected
    if expected is None:
        assert hb3.hw_07(month) is None


@pytest.mark.parametrize("p1, p2, expected", [
    ("камень", "ножницы", "игрок 1"),
    ("ножницы", "камень", "игрок 2"),
    ("бумага", "камень", "игрок 1"),
    ("ножницы", "бумага", "игрок 1"),
    ("бумага", "бумага", "ничья"),
])
def test_hw_08_rock_paper_scissors(p1, p2, expected):
    assert hb3.hw_08(p1, p2) == expected


@pytest.mark.parametrize("a, b_, c, expected", [
    (3, 4, 5, True),
    (5, 5, 5, True),
    (1, 1, 5, False),
    (1, 2, 3, False),
    (0, 1, 1, False),
    (-3, 4, 5, False),
])
def test_hw_09_triangle_exists(a, b_, c, expected):
    assert hb3.hw_09(a, b_, c) is expected


@pytest.mark.parametrize("n, expected", [
    (1, "год"),
    (2, "года"),
    (5, "лет"),
    (11, "лет"),
    (21, "год"),
    (22, "года"),
    (100, "лет"),
    (101, "год"),
    (111, "лет"),
    (112, "лет"),
    (0, "лет"),
])
def test_hw_10_year_word(n, expected):
    assert hb3.hw_10(n) == expected


@pytest.mark.parametrize("text, expected", [
    ("кот пёс кот кот пёс", "кот"),
    ("а б а б", "а"),
    ("один", "один"),
])
def test_hw_11_most_frequent_word(text, expected):
    assert hb4.hw_11(text) == expected


@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2], [3, 4]], [3, 7]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [6, 15, 24]),
    ([], []),
    ([[10]], [10]),
])
def test_hw_12_row_sums(matrix, expected):
    assert hb4.hw_12(matrix) == expected


@pytest.mark.parametrize("items, expected", [
    ([1, 2, 1, 3, 2], [1, 2, 3]),
    (["a", "b", "a", "a"], ["a", "b"]),
    ([], []),
])
def test_hw_13_dedup(items, expected):
    assert hb4.hw_13(items) == expected


@pytest.mark.parametrize("mapping, expected", [
    ({"a": 1, "b": 2}, {1: "a", 2: "b"}),
    ({}, {}),
    ({"x": (1, 2)}, {(1, 2): "x"}),
])
def test_hw_14_invert_dict(mapping, expected):
    assert hb4.hw_14(mapping) == expected


@pytest.mark.parametrize("n, expected", [
    (5, [0, 1, 1, 2, 3]),
    (1, [0]),
    (0, []),
    (8, [0, 1, 1, 2, 3, 5, 8, 13]),
])
def test_hw_15_fibonacci(n, expected):
    assert hb5.hw_15(n) == expected


@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (9, False),
    (97, True),
    (7919, True),
    (7917, False),
])
def test_hw_16_is_prime(n, expected):
    assert hb5.hw_16(n) is expected


def test_hw_17_fizzbuzz():
    assert hb5.hw_17(5) == ["1", "2", "fizz", "4", "buzz"]
    assert hb5.hw_17(0) == []
    full = hb5.hw_17(15)
    assert full[-1] == "fizzbuzz"
    assert full[2] == "fizz"
    assert full[4] == "buzz"
    assert len(full) == 15


def test_hw_18_parse_pair():
    assert hb6.hw_18("3 4") == (3, 4)
    assert hb6.hw_18("-1 10") == (-1, 10)
    assert hb6.hw_18("3") is None
    assert hb6.hw_18("3 x") is None
    assert hb6.hw_18("1 2 3") is None


def test_hw_19_read_lines(tmp_path):
    existing = tmp_path / "lines.txt"
    existing.write_text("раз\nдва\nтри\n", encoding="utf-8")
    missing = tmp_path / "no_such_file.txt"

    assert hb6.hw_19(str(existing)) == ["раз", "два", "три"]
    assert hb6.hw_19(str(missing)) == []


def test_hw_20_validate_age():
    assert hb6.hw_20(30) == 30
    assert hb6.hw_20(0) == 0
    assert hb6.hw_20(120) == 120
    with pytest.raises(TypeError, match="целым"):
        hb6.hw_20("30")
    with pytest.raises(TypeError, match="целым"):
        hb6.hw_20(12.0)
    with pytest.raises(ValueError, match="от 0 до 120"):
        hb6.hw_20(-1)
    with pytest.raises(ValueError, match="от 0 до 120"):
        hb6.hw_20(121)
