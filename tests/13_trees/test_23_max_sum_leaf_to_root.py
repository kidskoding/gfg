import pytest
from helpers import load
from helpers.trees import build

max_leaf_to_root_sum = load("13_trees.23_max_sum_leaf_to_root").max_leaf_to_root_sum


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3], 4),
        ([10, -2, 7, 8, -4], 17),
        ([1, -2, -3, 1, 3, -2, None, -1], 2),
        ([1, 2, 3, 4, 5, 6, 7], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 26),
        ([1, 100, 2, None, None, 3, 4], 101),  # heavy short path beats deep path
        ([1, 2, 3, 50], 53),  # deep path beats heavy sibling
        ([5, 1], 6),
        ([5, None, 1], 6),
        ([-5, -3, -10], -8),
        ([-1, None, -2, None, -3], -6),  # all negative, single path
        ([0, 0, 0], 0),
        ([-5], -5),
    ],
)
def test_max_leaf_to_root_sum(tree, expected):
    assert max_leaf_to_root_sum(build(tree)) == expected
