import pytest
from helpers import load
from helpers.trees import build, inorder, to_list

remove_outside_range = load("13_trees.27_remove_bst_keys_outside_range").remove_outside_range


@pytest.mark.parametrize(
    "tree, low, high, expected",
    [
        ([6, -13, 14, None, -8, 13, 15, None, None, 7], -10, 13, [6, -8, 13, None, None, 7]),
        ([10, 5, 15], 12, 20, [15]),
        ([10, 5, 15], 1, 20, [10, 5, 15]),
        ([10, 5, 15], 100, 200, []),
        ([], 1, 2, []),
    ],
)
def test_remove_outside_range(tree, low, high, expected):
    root = remove_outside_range(build(tree), low, high)
    assert to_list(root) == expected
    assert inorder(root) == sorted(inorder(root))
