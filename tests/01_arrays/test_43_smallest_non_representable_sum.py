import pytest
from helpers import load

smallest_non_representable = load(
    "01_arrays.43_smallest_non_representable_sum"
).smallest_non_representable


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], 7),
        ([3, 6, 9, 10, 20, 28], 1),
        ([1, 3, 6, 10, 11, 15], 2),
        ([1, 1, 1, 1], 5),
        ([1, 1, 3, 4], 10),
        ([1, 2, 5, 10, 20, 40], 4),
        ([1, 2, 3, 4, 5, 6], 22),
        ([], 1),
    ],
)
def test_smallest_non_representable(arr, expected):
    assert smallest_non_representable(arr) == expected
