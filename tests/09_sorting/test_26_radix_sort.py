import pytest
from helpers import load

radix_sort = load("09_sorting.26_radix_sort").radix_sort


@pytest.mark.parametrize(
    "arr",
    [
        [170, 45, 75, 90, 802, 24, 2, 66],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [1000, 1, 100, 10],
        [5, 5, 0],
        [0],
        [],
    ],
)
def test_radix_sort(arr):
    expected = sorted(arr)
    assert radix_sort(arr) is None
    assert arr == expected
