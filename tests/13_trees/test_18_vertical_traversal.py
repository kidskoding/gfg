import pytest
from helpers import load
from helpers.trees import build

vertical_order = load("13_trees.18_vertical_traversal").vertical_order


@pytest.mark.parametrize(
    "tree, expected",
    [
        (
            [1, 2, 3, 4, 5, 6, 7, None, None, None, None, None, None, 8, 9],
            [[4], [2], [1, 5, 6], [3, 8], [7], [9]],
        ),
        ([1, 2, 3, None, 4, 5], [[2], [1, 4, 5], [3]]),  # same column+level: level order
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        ([1, 2, 3, 4, 5, None, 6, None, None, 7], [[4], [2, 7], [1, 5], [3], [6]]),
        ([1, 2, 3, None, None, 4, None, 5], [[2, 5], [1, 4], [3]]),  # deep node lands in a far column
        ([1, 2], [[2], [1]]),
        ([1, None, 2], [[1], [2]]),
        ([1, 2, None, 3], [[3], [2], [1]]),  # left chain: one node per column
        ([1, None, 2, None, 3], [[1], [2], [3]]),
        ([1, 2, 3, None, 4, 5, None], [[2], [1, 4, 5], [3]]),
        ([1], [[1]]),
        ([], []),
    ],
)
def test_vertical_order(tree, expected):
    assert vertical_order(build(tree)) == expected
