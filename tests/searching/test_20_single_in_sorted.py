import pytest
from helpers import load

single_in_sorted = load("searching.20_single_in_sorted").single_in_sorted


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65], 4),
        ([1, 1, 3, 3, 4, 5, 5], 4),  # middle
        ([5, 5, 16, 16, 18, 18, 20], 20),  # last
        ([1, 2, 2], 1),  # first
        ([1, 1, 2], 2),
        ([-3, -3, -1, 0, 0], -1),
        ([7], 7),
    ],
)
def test_single_in_sorted(arr, expected):
    assert single_in_sorted(arr) == expected
