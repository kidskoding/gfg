import pytest
from helpers import load

closest_subsequence_sum = load(
    "arrays.42_closest_subsequence_sum"
).closest_subsequence_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([5, -7, 3, 5], 6, 0),
        ([1, 2, 3], -7, 7),
        ([7, -9, 15, -2], -5, 1),
        ([4, 8], 7, 1),
        ([], 3, 3),
        ([10], 4, 4),
        ([1, 1, 1, 1], 3, 0),
    ],
)
def test_closest_subsequence_sum(arr, target, expected):
    assert closest_subsequence_sum(arr, target) == expected
