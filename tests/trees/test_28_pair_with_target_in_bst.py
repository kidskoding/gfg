import pytest
from helpers import load
from helpers.trees import build

find_pair = load("trees.28_pair_with_target_in_bst").find_pair


@pytest.mark.parametrize(
    "tree, target, expected",
    [
        ([2, 1, 3], 4, True),
        ([2, 1, 3], 5, True),
        ([2, 1, 3], 6, False),
        ([2, 1, 3], 2, False),  # cannot reuse node 1
        ([10, 5, 15, 3, 7, None, 18], 25, True),
        ([10, 5, 15, 3, 7, None, 18], 22, True),
        ([10, 5, 15, 3, 7, None, 18], 36, False),
        ([1], 2, False),
        ([], 0, False),
    ],
)
def test_find_pair(tree, target, expected):
    assert find_pair(build(tree), target) is expected
