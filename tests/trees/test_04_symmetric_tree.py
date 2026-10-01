import pytest
from helpers import load
from helpers.trees import build

is_symmetric = load("trees.04_symmetric_tree").is_symmetric


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1, 2, 2, 3, None, None, 3], True),
        ([1, 2, 3], False),
        ([1], True),
        ([], True),
    ],
)
def test_is_symmetric(tree, expected):
    assert is_symmetric(build(tree)) is expected
