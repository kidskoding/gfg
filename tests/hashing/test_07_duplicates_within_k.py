import pytest
from helpers import load

has_duplicate_within_k = load("hashing.07_duplicates_within_k").has_duplicate_within_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 4, 1, 2, 3, 4], 3, False),
        ([1, 2, 3, 1, 4, 5], 3, True),
        ([1, 2, 3, 4, 5], 3, False),
        ([1, 2, 3, 4, 4], 3, True),
        ([1, 2, 1], 1, False),  # distance 2 > k
        ([7, 7], 1, True),
        ([7, 7], 0, False),
        ([], 2, False),
    ],
)
def test_has_duplicate_within_k(arr, k, expected):
    assert has_duplicate_within_k(arr, k) is expected
