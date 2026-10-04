import pytest
from helpers import load
from helpers.trees import build

single_valued_count = load("13_trees.15_single_valued_subtree").single_valued_count


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([5, 1, 5, 5, 5, None, 5], 4),
        ([5, 4, 5, 4, 4, None, 5], 5),
        ([5, 5, 5], 3),
        ([1], 1),
        ([], 0),
    ],
)
def test_single_valued_count(tree, expected):
    assert single_valued_count(build(tree)) == expected
