import pytest
from helpers import load

smallest_missing_positive = load(
    "arrays.40_smallest_missing_positive"
).smallest_missing_positive


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, -3, 4, 1, 1, 7], 3),
        ([5, 3, 2, 5, 1], 4),
        ([-8, 0, -1, -4, -3], 1),
        ([1, 2, 3], 4),
        ([], 1),
        ([7, 8, 9, 11, 12], 1),
        ([2, 2, 1, 1], 3),
    ],
)
def test_smallest_missing_positive(arr, expected):
    assert smallest_missing_positive(arr) == expected
