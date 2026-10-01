import pytest
from helpers import load
from helpers.trees import build

ancestors = load("trees.26_ancestors_in_binary_tree").ancestors


@pytest.mark.parametrize(
    "target, expected",
    [(7, [3, 1]), (4, [2, 1]), (2, [1]), (1, []), (8, [5, 2, 1]), (99, [])],
)
def test_ancestors(target, expected):
    assert ancestors(build([1, 2, 3, 4, 5, 6, 7, None, None, 8]), target) == expected
