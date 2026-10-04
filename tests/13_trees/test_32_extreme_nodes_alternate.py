import pytest
from helpers import load
from helpers.trees import build

extreme_alternate = load("13_trees.32_extreme_nodes_alternate").extreme_alternate


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [1, 3, 4, 15]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 4]),
        ([1, 2, None, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
    ],
)
def test_extreme_alternate(tree, expected):
    assert extreme_alternate(build(tree)) == expected
