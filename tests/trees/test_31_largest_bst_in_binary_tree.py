import pytest
from helpers import load
from helpers.trees import build

largest_bst_size = load("trees.31_largest_bst_in_binary_tree").largest_bst_size


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([5, 2, 4, 1, 3], 3),
        ([10, 5, 15, 1, 8, None, 7], 3),
        ([2, 1, 3], 3),
        ([20, 8, 22, 4, 12, None, None, None, None, 10, 14], 7),
        ([5, 4, 5, 4, 4, None, 5], 1),
        ([], 0),
    ],
)
def test_largest_bst_size(tree, expected):
    assert largest_bst_size(build(tree)) == expected
