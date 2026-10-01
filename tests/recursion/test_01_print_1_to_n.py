import pytest
from helpers import load

print_1_to_n = load("recursion.01_print_1_to_n").print_1_to_n


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, [1, 2, 3, 4, 5]),
        (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        (1, [1]),
        (2, [1, 2]),
        (0, []),
        (-3, []),
    ],
)
def test_print_1_to_n(n, expected):
    assert print_1_to_n(n) == expected


def test_print_1_to_n_large():
    assert print_1_to_n(500) == list(range(1, 501))
