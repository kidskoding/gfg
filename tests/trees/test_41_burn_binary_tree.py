import pytest
from helpers import load
from helpers.trees import build

burn_time = load("trees.41_burn_binary_tree").burn_time


@pytest.mark.parametrize(
    "tree, target, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 4, 4),
        ([1, 2, 3, 4, 5, 6, 7], 1, 2),
        ([1, 2, 3, None, None, 4, 5], 3, 2),
        ([1, 2, None, 3, None, 4, None, 5], 3, 2),
        ([1, 2, None, 3, None, 4, None, 5], 1, 4),
        ([1], 1, 0),
    ],
)
def test_burn_time(tree, target, expected):
    assert burn_time(build(tree), target) == expected
