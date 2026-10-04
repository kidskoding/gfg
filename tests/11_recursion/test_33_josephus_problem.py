import pytest
from helpers import load

josephus = load("11_recursion.33_josephus_problem").josephus


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (5, 2, 3),
        (7, 3, 4),
        (14, 2, 13),
        (41, 3, 31),
        (6, 6, 4),
        (5, 1, 5),  # k == 1: last person survives
        (2, 2, 1),
        (1, 4, 1),
    ],
)
def test_josephus(n, k, expected):
    assert josephus(n, k) == expected
