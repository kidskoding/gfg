import pytest
from helpers import load
from helpers.trees import to_list

bst_from_preorder = load("trees.21_bst_from_preorder").bst_from_preorder


@pytest.mark.parametrize(
    "pre, expected",
    [
        ([10, 5, 1, 7, 40, 50], [10, 5, 40, 1, 7, None, 50]),
        ([8, 5, 1, 7, 10, 12], [8, 5, 10, 1, 7, None, 12]),
        ([1, 2, 3], [1, None, 2, None, 3]),
        ([3, 2, 1], [3, 2, None, 1]),
        ([], []),
    ],
)
def test_bst_from_preorder(pre, expected):
    assert to_list(bst_from_preorder(pre)) == expected
