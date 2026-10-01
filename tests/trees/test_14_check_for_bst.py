import pytest
from helpers import load
from helpers.trees import build

is_bst = load("trees.14_check_for_bst").is_bst


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([2, 1, 3], True),
        ([2, 3, 1], False),
        ([10, 5, 20, None, None, 9, 25], False),  # 9 in right subtree of 10
        ([10, 5, 20, 1, 11], False),  # 11 in left subtree of 10
        ([5, 5], False),  # duplicates not allowed
        ([20, 8, 22, 4, 12, None, None, None, None, 10, 14], True),
        ([1], True),
        ([], True),
    ],
)
def test_is_bst(tree, expected):
    assert is_bst(build(tree)) is expected
