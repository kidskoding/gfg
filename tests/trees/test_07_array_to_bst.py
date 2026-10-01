import pytest
from helpers import load
from helpers.trees import edge_height, inorder, is_height_balanced

sorted_array_to_bst = load("trees.07_array_to_bst").sorted_array_to_bst


@pytest.mark.parametrize("arr", [[1], [1, 2], [1, 2, 3, 4, 5, 6, 7], list(range(1, 21))])
def test_sorted_array_to_bst(arr):
    root = sorted_array_to_bst(arr)
    assert inorder(root) == arr
    assert is_height_balanced(root)
    assert edge_height(root) == len(arr).bit_length() - 1


def test_sorted_array_to_bst_empty():
    assert sorted_array_to_bst([]) is None
