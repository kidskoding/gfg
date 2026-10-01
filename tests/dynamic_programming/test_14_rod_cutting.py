import pytest
from helpers import load

rod_cutting = load("dynamic_programming.14_rod_cutting").rod_cutting


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1, 5, 8, 9, 10, 17, 17, 20], 22),
        ([3, 5, 8, 9, 10, 17, 17, 20], 24),
        ([1, 10, 3], 11),
        ([2, 5, 7, 8], 10),
        ([3], 3),
        ([], 0),
    ],
)
def test_rod_cutting(prices, expected):
    assert rod_cutting(prices) == expected
