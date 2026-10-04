import pytest
from helpers import load
from helpers.trees import build, find

lca = load("13_trees.25_lowest_common_ancestor").lca


@pytest.mark.parametrize(
    "a, b, expected", [(4, 5, 2), (4, 6, 1), (2, 4, 2), (4, 4, 4), (1, 7, 1), (6, 7, 3)]
)
def test_lca(a, b, expected):
    root = build([1, 2, 3, 4, 5, 6, 7])
    assert lca(root, a, b) is find(root, expected)
