import pytest
from helpers import load
from helpers.trees import build, to_list

to_greater_sum_tree = load("trees.29_bst_to_greater_sum_tree").to_greater_sum_tree


@pytest.mark.parametrize(
    "tree, expected",
    [
        (
            [11, 2, 29, 1, 7, 15, 40, None, None, None, None, None, None, 35],
            [119, 137, 75, 139, 130, 104, 0, None, None, None, None, None, None, 40],
        ),
        (
            [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
            [26, 35, 15, 36, 33, 21, 8, None, None, None, 30, None, None, None, 0],
        ),
        ([2, 1, 3], [3, 5, 0]),
        ([1, None, 2, None, 3], [5, None, 3, None, 0]),  # right chain
        ([3, 2, None, 1], [0, 3, None, 5]),  # left chain
        ([0, -3, 5], [5, 5, 0]),  # negatives
        ([5, 3, 8, 1, 4, 7, 9], [24, 33, 9, 36, 29, 17, 0]),
        ([1], [0]),
        ([], []),
    ],
)
def test_to_greater_sum_tree(tree, expected):
    root = build(tree)
    to_greater_sum_tree(root)
    assert to_list(root) == expected


@pytest.mark.parametrize(
    "tree",
    [
        [20, 8, 22, 4, 12, None, None, None, None, 10, 14],
        [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 90],
        [10, 5, 15, 2, None, None, 20, 1, None, None, 25],
        [-10, -20, 0, -30, -15, -5, 5],
    ],
)
def test_to_greater_sum_tree_matches_definition(tree):
    """Each node becomes the sum of every key strictly greater than its own."""
    keys = [v for v in tree if v is not None]
    expected = [sum(k for k in keys if k > v) if v is not None else None for v in tree]
    root = build(tree)
    to_greater_sum_tree(root)
    assert to_list(root) == expected
