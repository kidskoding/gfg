import pytest
from helpers import load

first_n_fibonacci = load("11_recursion.11_first_n_fibonacci").first_n_fibonacci


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, [0, 1, 1, 2, 3]),
        (7, [0, 1, 1, 2, 3, 5, 8]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        (1, [0]),
        (2, [0, 1]),
        (0, []),
    ],
)
def test_first_n_fibonacci(n, expected):
    assert first_n_fibonacci(n) == expected


def test_first_n_fibonacci_tail():
    assert first_n_fibonacci(40)[-1] == 63245986
