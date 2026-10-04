import pytest
from helpers import load
from helpers.trees import build

is_min_heap = load("14_heaps.11_is_min_heap").is_min_heap


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
        ([5, 6, 7, 8], True),
        ([1, 1, 1], True),  # equal values allowed
        ([1, 2], True),
        ([10, 9, 8, 7, 6, 5, 4], False),  # max heap, not min heap
        ([2, 1], False),
        ([1, 2, 3, 4, 5, 6, 0], False),  # violation deep in the tree
        ([1, 2, 3, None, 4], False),  # not complete
        ([5, 6, 7, None, None, 8], False),  # not complete
        ([1, None, 2], False),  # missing left child
        ([1], True),
        ([], True),
    ],
)
def test_is_min_heap(tree, expected):
    assert is_min_heap(build(tree)) is expected
