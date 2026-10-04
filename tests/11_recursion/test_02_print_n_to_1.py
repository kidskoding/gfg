import pytest
from helpers import load

print_n_to_1 = load("11_recursion.02_print_n_to_1").print_n_to_1


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, [5, 4, 3, 2, 1]),
        (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
        (1, [1]),
        (2, [2, 1]),
        (0, []),
        (-1, []),
    ],
)
def test_print_n_to_1(n, expected):
    assert print_n_to_1(n) == expected


def test_print_n_to_1_large():
    assert print_n_to_1(500) == list(range(500, 0, -1))
