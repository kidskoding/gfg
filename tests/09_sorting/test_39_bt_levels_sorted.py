import pytest
from helpers import load
from helpers.trees import build

levels_sorted = load("09_sorting.39_bt_levels_sorted").levels_sorted


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([7, 6, 5, 4, 3, 2, 1], [[7], [5, 6], [1, 2, 3, 4]]),
        ([5, 6, 4, 9, 2], [[5], [4, 6], [2, 9]]),
        ([10, 3, 3, 1, None, None, -2], [[10], [3, 3], [-2, 1]]),
        ([1, None, 3, None, 2], [[1], [3], [2]]),
        ([1], [[1]]),
        ([], []),
    ],
)
def test_levels_sorted(tree, expected):
    assert levels_sorted(build(tree)) == expected
