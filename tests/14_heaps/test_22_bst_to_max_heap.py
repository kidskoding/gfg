import pytest
from helpers import load
from helpers.trees import build, to_list

bst_to_max_heap = load("14_heaps.22_bst_to_max_heap").bst_to_max_heap


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([4, 2, 6, 1, 3, 5, 7], [7, 3, 6, 1, 2, 4, 5]),
        ([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7], [14, 7, 12, 3, 6, 8, 10, 1, 2, 4, 5]),
        ([2, 1, 3], [3, 1, 2]),
        ([2, 1], [2, 1]),
        ([1], [1]),
        ([], []),
    ],
)
def test_bst_to_max_heap(tree, expected):
    root = build(tree)
    left = root.left if root else None
    assert bst_to_max_heap(root) is None
    assert to_list(root) == expected
    if root:
        assert root.left is left  # values rewritten, nodes kept
