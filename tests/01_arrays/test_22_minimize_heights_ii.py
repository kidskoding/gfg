import pytest
from helpers import load

minimize_heights = load("01_arrays.22_minimize_heights_ii").minimize_heights


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 5, 8, 10], 2, 5),
        ([3, 9, 12, 16, 20], 3, 11),
        ([1, 5, 15, 10], 3, 8),
        ([7, 7, 7], 4, 0),
        ([5], 10, 0),
        ([1, 2], 5, 1),
        ([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 5, 7),
    ],
)
def test_minimize_heights(arr, k, expected):
    assert minimize_heights(arr, k) == expected
