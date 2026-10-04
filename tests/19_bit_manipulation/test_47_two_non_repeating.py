import pytest
from helpers import load

two_non_repeating = load("19_bit_manipulation.47_two_non_repeating").two_non_repeating


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 4, 7, 9, 2, 4], [7, 9]),
        ([1, 2, 3, 2, 1, 4], [3, 4]),
        ([2, 1, 3, 2], [1, 3]),
        ([6, 5], [5, 6]),
        ([-1, 0, 0, 3], [-1, 3]),
        ([0, 1], [0, 1]),
    ],
)
def test_two_non_repeating(arr, expected):
    assert two_non_repeating(arr) == expected
