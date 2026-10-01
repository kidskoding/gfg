import pytest
from helpers import load
from helpers.trees import build

kth_largest = load("trees.10_kth_largest_in_bst").kth_largest


@pytest.mark.parametrize(
    "tree, k, expected",
    [
        ([4, 2, 9], 1, 9),
        ([4, 2, 9], 2, 4),
        ([4, 2, 9], 3, 2),
        ([9, 8, None, 7, None, 6], 3, 7),
        ([20, 8, 22, 4, 12, None, None, None, None, 10, 14], 4, 12),
    ],
)
def test_kth_largest(tree, k, expected):
    assert kth_largest(build(tree), k) == expected
