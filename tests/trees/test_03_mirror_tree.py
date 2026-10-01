import pytest
from helpers import load
from helpers.trees import build, to_list

mirror = load("trees.03_mirror_tree").mirror


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5], [1, 3, 2, None, None, 5, 4]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4]),
        ([1, 2, 3, None, 4, 5], [1, 3, 2, None, 5, 4]),
        ([1, 2], [1, None, 2]),  # left child moves right
        ([1, None, 2], [1, 2]),  # right child moves left
        ([1, None, 2, None, 3], [1, 2, None, 3]),  # right chain becomes left chain
        ([1, 2, None, 3, None, 4], [1, None, 2, None, 3, None, 4]),
        ([1, 2, 2, 3, 4, 4, 3], [1, 2, 2, 3, 4, 4, 3]),  # symmetric: unchanged
        ([7, 7, 7, 7, 7], [7, 7, 7, None, None, 7, 7]),  # same values, structure still flips
        ([1], [1]),
        ([], []),
    ],
)
def test_mirror(tree, expected):
    root = build(tree)
    mirror(root)
    assert to_list(root) == expected


@pytest.mark.parametrize(
    "tree",
    [
        [1, 2, None, 3, 4],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [1, None, 2, 3, None, None, 4],
        [5, 3, 8, 1, 4, 7, 9, None, 2],
        [1],
    ],
)
def test_mirror_twice_restores(tree):
    root = build(tree)
    mirror(root)
    mirror(root)
    assert to_list(root) == tree


def test_mirror_is_in_place():
    root = build([1, 2, 3])
    left, right = root.left, root.right
    mirror(root)
    assert root.left is right
    assert root.right is left


def test_mirror_empty_does_not_crash():
    mirror(None)
