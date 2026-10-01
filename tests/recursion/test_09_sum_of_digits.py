import pytest
from helpers import load

sum_of_digits = load("recursion.09_sum_of_digits").sum_of_digits


@pytest.mark.parametrize(
    "n, expected",
    [
        (12345, 15),
        (45632, 20),
        (687, 21),
        (7, 7),
        (0, 0),
        (1000, 1),
        (99999, 45),
    ],
)
def test_sum_of_digits(n, expected):
    assert sum_of_digits(n) == expected
