import pytest
from helpers import load

module = load("09_sorting.14_kth_smallest_largest")
kth_smallest, kth_largest = module.kth_smallest, module.kth_largest

CASES = [
    ([7, 10, 4, 3, 20, 15], 3, 7, 10),
    ([2, 3, 1, 20, 15], 4, 15, 2),
    ([4, 4, 1, 4], 2, 4, 4),
    ([-1, -5, 3], 1, -5, 3),
    ([9, 8, 7, 6, 5], 5, 9, 5),
    ([5], 1, 5, 5),
]


@pytest.mark.parametrize("arr, k, smallest, largest", CASES)
def test_kth_smallest(arr, k, smallest, largest):
    original = list(arr)
    assert kth_smallest(arr, k) == smallest
    assert arr == original


@pytest.mark.parametrize("arr, k, smallest, largest", CASES)
def test_kth_largest(arr, k, smallest, largest):
    original = list(arr)
    assert kth_largest(arr, k) == largest
    assert arr == original
