import pytest
from helpers import load

search_rotated = load("10_searching.11_search_rotated_sorted").search_rotated


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        ([5, 6, 7, 8, 9, 10, 1, 2, 3], 3, 8),
        ([5, 6, 7, 8, 9, 10, 1, 2, 3], 30, -1),
        ([5, 6, 7, 8, 9, 10, 1, 2, 3], 5, 0),
        ([30, 40, 50, 10, 20], 10, 3),
        ([4, 5, 1, 2, 3], 5, 1),
        ([1, 2, 3, 4], 1, 0),  # not rotated
        ([3, 1], 1, 1),
        ([1], 1, 0),
        ([1], 0, -1),
        ([], 1, -1),
    ],
)
def test_search_rotated(arr, key, expected):
    assert search_rotated(arr, key) == expected
