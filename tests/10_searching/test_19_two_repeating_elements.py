import pytest
from helpers import load

two_repeating = load("10_searching.19_two_repeating_elements").two_repeating


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 2, 4, 5, 2, 3, 1], [2, 4]),
        ([2, 1, 2, 1, 3], [1, 2]),
        ([3, 1, 3, 1, 2], [1, 3]),
        ([5, 4, 3, 2, 1, 5, 1], [1, 5]),
        ([1, 1, 2, 2], [1, 2]),  # adjacent duplicates
        ([1, 2, 1, 2], [1, 2]),
    ],
)
def test_two_repeating(arr, expected):
    assert list(two_repeating(arr)) == expected
