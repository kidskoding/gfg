import pytest
from helpers import load

smallest_diff_triplet = load("09_sorting.36_smallest_diff_triplet").smallest_diff_triplet


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        ([5, 2, 8], [10, 7, 12], [9, 14, 6], [5, 6, 7]),
        ([15, 12, 18, 9], [10, 17, 13, 8], [14, 16, 11, 5], [9, 10, 11]),
        ([1, 5], [2, 6], [3, 7], [1, 2, 3]),  # tie on diff: smaller sum wins
        ([1, 100], [2, 200], [3, 300], [1, 2, 3]),
        ([-10, 0], [-9, 20], [-8, 30], [-10, -9, -8]),
        ([1], [1], [1], [1, 1, 1]),
    ],
)
def test_smallest_diff_triplet(a, b, c, expected):
    assert list(smallest_diff_triplet(a, b, c)) == expected
