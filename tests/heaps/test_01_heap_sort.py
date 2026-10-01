import pytest
from helpers import load

heap_sort = load("heaps.01_heap_sort").heap_sort


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 1, 3, 9, 7], [1, 3, 4, 7, 9]),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
        ([-1, -5, 0, 2], [-5, -1, 0, 2]),
        ([3, 3, 3], [3, 3, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
    ],
)
def test_heap_sort(arr, expected):
    assert heap_sort(arr) is None
    assert arr == expected
