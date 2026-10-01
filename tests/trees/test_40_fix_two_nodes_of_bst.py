import pytest
from helpers import load
from helpers.trees import build, to_list

fix_bst = load("trees.40_fix_two_nodes_of_bst").fix_bst


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([10, 5, 8, 2, 20], [10, 5, 20, 2, 8]),
        ([1, 3, None, None, 2], [3, 1, None, None, 2]),  # adjacent in inorder
        ([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3]),
        ([20, 8, 22, 4, 12, None, None, None, None, 14, 10], [20, 8, 22, 4, 12, None, None, None, None, 10, 14]),
        ([2, 3, 1], [2, 1, 3]),  # two leaves swapped
        ([1, 2, 3], [2, 1, 3]),  # root swapped with left child
        ([4, 6, 2, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),  # both children of root swapped
        ([4, 2, 6, 7, 3, 5, 1], [4, 2, 6, 1, 3, 5, 7]),  # outermost leaves swapped
        ([1, 2, 6, 4, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),  # root swapped with a leaf
        ([4, 2, 6, 1, 5, 3, 7], [4, 2, 6, 1, 3, 5, 7]),  # inner nodes across subtrees
        ([2, None, 1], [1, None, 2]),  # two-node chain
    ],
)
def test_fix_bst(tree, expected):
    root = build(tree)
    fix_bst(root)
    assert to_list(root) == expected
