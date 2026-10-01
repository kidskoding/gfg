import pytest
from helpers import load
from helpers.trees import build

odd_even_diff = load("trees.24_odd_even_level_difference").odd_even_diff


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([5, 2, 6, 1, 4, None, 8], 10),
        ([1, 2, 3], -4),
        ([1, 2, 3, 4, 5, 6, 7], 18),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], -74),
        ([1, 2, None, 3, None, 4], -2),  # chain: levels alternate sign
        ([10, 20, 30, 40, None, None, 50, 60], -10),
        ([-1, -2, -3], 4),
        ([1, 1, 1, 1, 1, 1, 1], 3),
        ([1, 2], -1),
        ([1, None, 2], -1),
        ([1], 1),
        ([], 0),
    ],
)
def test_odd_even_diff(tree, expected):
    assert odd_even_diff(build(tree)) == expected
