import pytest
from helpers import load
from helpers.trees import build

is_balanced = load("13_trees.05_balanced_tree").is_balanced


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5], True),
        ([1, 2, None, 3], False),
        ([1, 2, 3, 4, None, None, None, 5], False),
        ([1, 2, 3, 4, 5, 6, 7], True),
        ([1], True),
        ([], True),
    ],
)
def test_is_balanced(tree, expected):
    assert is_balanced(build(tree)) is expected
