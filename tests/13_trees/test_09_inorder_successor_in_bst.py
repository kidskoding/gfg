import pytest
from helpers import load
from helpers.trees import build

inorder_successor = load("13_trees.09_inorder_successor_in_bst").inorder_successor


@pytest.mark.parametrize(
    "x, expected",
    [(8, 10), (10, 12), (14, 20), (20, 22), (22, -1), (4, 8), (12, 14)],
)
def test_inorder_successor(x, expected):
    root = build([20, 8, 22, 4, 12, None, None, None, None, 10, 14])
    assert inorder_successor(root, x) == expected
