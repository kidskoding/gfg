import pytest
from helpers import load
from helpers.heaps import is_max_heap

min_heap_to_max_heap = load("heaps.10_min_heap_to_max_heap").min_heap_to_max_heap


@pytest.mark.parametrize(
    "arr",
    [
        [3, 5, 9, 6, 8, 20, 10, 12, 18, 9],
        [1, 2, 3, 4],
        [1, 2, 3],
        [-5, -3, -4, 0],
        [1, 1, 1],
        [7],
        [],
    ],
)
def test_min_heap_to_max_heap(arr):
    original = sorted(arr)
    assert min_heap_to_max_heap(arr) is None
    assert sorted(arr) == original
    assert is_max_heap(arr)
