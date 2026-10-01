import pytest
from helpers import load

plus_one = load("arrays.10_plus_one").plus_one


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1, 2, 4], [1, 2, 5]),
        ([9, 9, 9], [1, 0, 0, 0]),
        ([1, 2, 9], [1, 3, 0]),
        ([0], [1]),
        ([9], [1, 0]),
        ([8, 9, 9, 9], [9, 0, 0, 0]),
    ],
)
def test_plus_one(digits, expected):
    assert plus_one(digits) == expected
