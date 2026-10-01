import pytest
from helpers import load
from helpers.trees import build

max_leaf_path_sum = load("trees.36_max_sum_path_between_leaves").max_leaf_path_sum


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([3, 4, 5, -10, 4], 16),
        (
            [-15, 5, 6, -8, 1, 3, 9, 2, 6, None, None, None, None, None, 0,
             None, None, None, None, 4, -1, None, None, 10],
            27,
        ),
        ([1, 2, 3], 6),
        ([-1, -2, -3], -6),
        ([1, 2, None, 3, 4], 9),  # both leaves under one child; path avoids root
    ],
)
def test_max_leaf_path_sum(tree, expected):
    assert max_leaf_path_sum(build(tree)) == expected
