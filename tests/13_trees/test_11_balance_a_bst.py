import pytest
from helpers import load
from helpers.trees import build, inorder, is_height_balanced

balance_bst = load("13_trees.11_balance_a_bst").balance_bst


@pytest.mark.parametrize(
    "tree",
    [
        [1, None, 2, None, 3, None, 4],
        [4, 3, None, 2, None, 1],
        [10, 5, 15, 2, None, None, 20, 1, None, None, 25],
        [1],
    ],
)
def test_balance_bst(tree):
    original = build(tree)
    root = balance_bst(original)
    assert inorder(root) == inorder(build(tree))
    assert is_height_balanced(root)


def test_balance_bst_empty():
    assert balance_bst(None) is None
