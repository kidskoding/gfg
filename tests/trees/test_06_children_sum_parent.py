import pytest
from helpers import load
from helpers.trees import build

is_sum_property = load("trees.06_children_sum_parent").is_sum_property


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([10, 8, 2, 3, 5], True),
        ([10, 7, 2], False),
        ([10, 10], True),
        ([10, 8, 2, 3, 5, None, None, 1, 2], True),
        ([10, 8, 2, 3, 5, None, None, 1, 1], False),
        ([5], True),
        ([], True),
    ],
)
def test_is_sum_property(tree, expected):
    assert is_sum_property(build(tree)) is expected
