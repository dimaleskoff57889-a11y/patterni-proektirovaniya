"""Тесты к теме 6 «Ошибки и исключения» (задания 31–36)."""

import pytest

from tasks import t06_exceptions as ex


def test_task_31_safe_div():
    assert ex.task_31(7, 2) == pytest.approx(3.5)
    assert ex.task_31(9, 3) == 3.0
    assert ex.task_31(1, 0) is None


def test_task_32_parse_int():
    assert ex.task_32("42") == 42
    assert ex.task_32("-7") == -7
    assert ex.task_32("4.2") is None
    assert ex.task_32("abc") is None
    assert ex.task_32("") is None


def test_task_33_first_line(tmp_path):
    existing = tmp_path / "note.txt"
    existing.write_text("привет\nмир\n", encoding="utf-8")
    empty = tmp_path / "empty.txt"
    empty.write_text("", encoding="utf-8")
    missing = tmp_path / "missing.txt"

    assert ex.task_33(str(existing)) == "привет"
    assert ex.task_33(str(empty)) == ""
    assert ex.task_33(str(missing)) == ""


def test_task_34_raise_on_negative():
    assert ex.task_34(5) == 5
    assert ex.task_34(0) == 0
    with pytest.raises(ValueError, match="неотрицательное"):
        ex.task_34(-1)


def test_task_35_get_or_message():
    assert ex.task_35([10, 20, 30], 1) == 20
    assert ex.task_35([10, 20, 30], -1) == 30
    assert ex.task_35([10, 20, 30], 5) == "индекс вне диапазона"
    assert ex.task_35([], 0) == "индекс вне диапазона"


def test_task_36_universal_parse():
    assert ex.task_36("7") == 7
    assert isinstance(ex.task_36("7"), int)
    assert ex.task_36("7.5") == 7.5
    assert isinstance(ex.task_36("7.5"), float)
    assert ex.task_36("abc") is None
