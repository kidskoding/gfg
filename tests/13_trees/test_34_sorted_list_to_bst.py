import pytest
from helpers import load
from helpers.trees import build_list, inorder, is_height_balanced

sorted_list_to_bst = load("13_trees.34_sorted_list_to_bst").sorted_list_to_bst


@pytest.mark.parametrize("values", [[1], [1, 2], [1, 2, 3, 4, 5, 6, 7], list(range(1, 21))])
def test_sorted_list_to_bst(values):
    root = sorted_list_to_bst(build_list(values))
    assert inorder(root) == values
    assert is_height_balanced(root)


def test_sorted_list_to_bst_empty():
    assert sorted_list_to_bst(None) is None
