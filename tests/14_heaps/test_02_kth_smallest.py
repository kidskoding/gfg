import pytest
from helpers import load

kth_smallest = load("14_heaps.02_kth_smallest").kth_smallest


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([7, 10, 4, 3, 20, 15], 3, 7),
        ([7, 10, 4, 20, 15], 4, 15),
        ([2, 2, 1], 2, 2),
        ([-3, -1, -2], 1, -3),
        ([1, 2, 3, 4], 4, 4),
        ([5], 1, 5),
    ],
)
def test_kth_smallest(arr, k, expected):
    assert kth_smallest(arr, k) == expected
