import pytest
from helpers import load

inversion_count = load("sorting.15_inversion_count").inversion_count


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 4, 1, 3, 5], 3),
        ([1, 20, 6, 4, 5], 5),
        ([5, 4, 3, 2, 1], 10),
        ([2, 3, 4, 5, 6], 0),
        ([10, 10, 10], 0),  # equal values are not inversions
        ([3, -1, 2], 2),
        ([], 0),
    ],
)
def test_inversion_count(arr, expected):
    original = list(arr)
    assert inversion_count(arr) == expected
    assert arr == original
