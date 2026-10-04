import pytest
from helpers import load
from helpers.trees import to_list

build_from_pre_in = load("13_trees.20_tree_from_preorder_inorder").build_from_pre_in


@pytest.mark.parametrize(
    "pre, ino, expected",
    [
        ([1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [1, 2, 3, 4, 5]),
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([1, 2, 3], [3, 2, 1], [1, 2, None, 3]),
        ([1], [1], [1]),
        ([], [], []),
    ],
)
def test_build_from_pre_in(pre, ino, expected):
    assert to_list(build_from_pre_in(pre, ino)) == expected
