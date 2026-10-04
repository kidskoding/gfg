import pytest
from helpers import load
from helpers.trees import build

boundary = load("13_trees.19_boundary_traversal").boundary


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9], [1, 2, 4, 8, 9, 6, 7, 3]),
        ([1, 2, 3, None, 4, 5, None, 6, None, None, 7], [1, 2, 4, 6, 7, 5, 3]),
        ([1, None, 2, 3, 4], [1, 3, 4, 2]),
        ([1, 2, None, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
    ],
)
def test_boundary(tree, expected):
    assert boundary(build(tree)) == expected
