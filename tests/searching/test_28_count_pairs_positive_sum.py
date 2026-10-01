import pytest
from helpers import load

count_pairs_positive_sum = load(
    "searching.28_count_pairs_positive_sum"
).count_pairs_positive_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, -2, 1], 2),
        ([-1, -1, -1, 0], 0),
        ([-1, -1, -1, 0, 1, 2], 6),
        ([1, 1, 1], 3),
        ([0, 0, 1], 2),
        ([-2, 2], 0),  # sum exactly 0 does not count
        ([5], 0),
        ([], 0),
    ],
)
def test_count_pairs_positive_sum(arr, expected):
    assert count_pairs_positive_sum(arr) == expected
