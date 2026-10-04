import pytest
from helpers import load

count_pairs_with_diff_k = load(
    "04_two_pointers.14_count_pairs_diff_k"
).count_pairs_with_diff_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 4, 1, 4, 5], 3, 4),
        ([8, 16, 12, 16, 4, 0], 4, 5),
        ([-1, 3, -5], 4, 2),
        ([1, 2, 3], 5, 0),
        ([2, 2, 2], 0, 3),
        ([7], 0, 0),
        ([], 1, 0),
    ],
)
def test_count_pairs_with_diff_k(arr, k, expected):
    assert count_pairs_with_diff_k(arr, k) == expected
