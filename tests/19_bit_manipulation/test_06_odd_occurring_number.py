import pytest
from helpers import load

odd_occurring = load("19_bit_manipulation.06_odd_occurring_number").odd_occurring


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 2, 3, 1, 3], 3),
        ([5, 7, 2, 7, 5, 2, 5], 5),
        ([9, 9, 8, 8, 9, 9, 7], 7),
        ([2, 2, 2], 2),
        ([-1, -1, -3], -3),
        ([0, 1, 1], 0),
        ([4], 4),
    ],
)
def test_odd_occurring(arr, expected):
    assert odd_occurring(arr) == expected
