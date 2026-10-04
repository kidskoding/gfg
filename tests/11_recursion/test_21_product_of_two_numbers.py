import pytest
from helpers import load

product = load("11_recursion.21_product_of_two_numbers").product


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (5, 2, 10),
        (100, 5, 500),
        (3, 7, 21),
        (0, 9, 0),
        (9, 0, 0),
        (1, 1, 1),
        (-4, 6, -24),
        (4, -6, -24),
        (-3, -5, 15),
    ],
)
def test_product(x, y, expected):
    assert product(x, y) == expected
