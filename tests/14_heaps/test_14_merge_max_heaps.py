import pytest
from helpers import load
from helpers.heaps import is_max_heap

merge_max_heaps = load("14_heaps.14_merge_max_heaps").merge_max_heaps


@pytest.mark.parametrize(
    "a, b",
    [
        ([10, 5, 6, 2], [12, 7, 9]),
        ([9, 8, 7], [20, 1]),
        ([5, 5], [5]),
        ([3, 1], []),
        ([], [4, 2, 3]),
        ([], []),
    ],
)
def test_merge_max_heaps(a, b):
    expected = sorted(a + b)
    result = merge_max_heaps(a, b)
    assert sorted(result) == expected
    assert is_max_heap(result)
