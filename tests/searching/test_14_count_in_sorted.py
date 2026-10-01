import pytest
from helpers import load

count_occurrences = load("searching.14_count_in_sorted").count_occurrences


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 1, 2, 2, 2, 2, 3], 2, 4),
        ([1, 1, 2, 2, 2, 2, 3], 4, 0),
        ([1, 1, 2, 2, 2, 2, 3], 1, 2),  # at the start
        ([1, 1, 2, 2, 2, 2, 3], 3, 1),  # at the end
        ([8, 8, 8], 8, 3),
        ([1, 2, 3], 0, 0),
        ([5], 5, 1),
        ([], 1, 0),
    ],
)
def test_count_occurrences(arr, target, expected):
    assert count_occurrences(arr, target) == expected
