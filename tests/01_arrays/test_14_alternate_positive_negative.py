import pytest
from helpers import load

rearrange_alternate = load("01_arrays.14_alternate_positive_negative").rearrange_alternate


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, -4, -1, 4], [1, -4, 2, -1, 3, 4]),
        ([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8], [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]),
        ([9, 4, -2, -1, 5, 0, -5, -3, 2], [9, -2, 4, -1, 5, -5, 0, -3, 2]),
        ([-1, -2, -3, 4], [4, -1, -2, -3]),
        ([1, 2, 3], [1, 2, 3]),
        ([-1], [-1]),
        ([], []),
    ],
)
def test_rearrange_alternate(arr, expected):
    rearrange_alternate(arr)
    assert arr == expected
