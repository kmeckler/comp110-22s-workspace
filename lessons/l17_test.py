"""Tests for the sum function."""


from lessons.l17_sum import sum


def test_sum_empty() -> None:
    assert sum([]) == 0.0


def test_sum_single() -> None:
    assert sum([110.0]) == 110.0


def test_sum_multiple() -> None:
    assert sum([1.0, 2.0, 3.0]) == 6.0 


def test_sum_two() -> None:
    assert sum([-1.0, 1.0]) == 0.0