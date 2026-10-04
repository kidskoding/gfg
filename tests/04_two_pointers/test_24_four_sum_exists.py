import pytest
from helpers import load

has_four_sum = load("04_two_pointers.24_four_sum_exists").has_four_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([10, 2, 3, 4, 5, 9, 7, 8], 23, True),
        ([-1, 0, 1, 2, -1, -4], -1, True),
        ([1, 2, 3, 4], 100, False),
        ([1, 1, 1, 1], 4, True),
        ([0, 0, 0, 0], 0, True),
        ([1, 1, 1], 3, False),  # fewer than four elements
        ([1, 2, 3], 6, False),
        ([], 0, False),
    ],
)
def test_has_four_sum(arr, target, expected):
    assert has_four_sum(arr, target) is expected
