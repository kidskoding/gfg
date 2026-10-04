import pytest
from helpers import load

sum_natural = load("11_recursion.04_sum_of_natural_numbers").sum_natural


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 15),
        (10, 55),
        (1, 1),
        (2, 3),
        (100, 5050),
        (0, 0),
        (-5, 0),
    ],
)
def test_sum_natural(n, expected):
    assert sum_natural(n) == expected
