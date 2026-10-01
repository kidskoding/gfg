import pytest
from helpers import load
from helpers.trees import build

max_non_adjacent_sum = load("trees.30_max_sum_non_adjacent").max_non_adjacent_sum


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([11, 1, 2], 11),
        ([1, 2, 3, 4, 5, 6], 16),
        ([3, 2, 3, None, 3, None, 1], 7),
        ([3, 4, 5, 1, 3, None, 1], 9),
        ([1], 1),
        ([], 0),
    ],
)
def test_max_non_adjacent_sum(tree, expected):
    assert max_non_adjacent_sum(build(tree)) == expected
