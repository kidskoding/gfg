import pytest
from helpers import load
from helpers.trees import build

merge_bsts = load("13_trees.39_merge_two_bsts").merge_bsts


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([5, 3, 6, 2, 4], [2, 1, 3, None, None, None, 7], [1, 2, 2, 3, 3, 4, 5, 6, 7]),
        ([2, 1, 3], [5, 4, 6], [1, 2, 3, 4, 5, 6]),  # disjoint, a below b
        ([5, 4, 6], [2, 1, 3], [1, 2, 3, 4, 5, 6]),  # disjoint, a above b
        ([4, 2, 6], [5, 3, 7, 1], [1, 2, 3, 4, 5, 6, 7]),  # interleaved
        ([1, None, 2], [1, None, 2], [1, 1, 2, 2]),  # identical trees
        ([1, None, 2, None, 3], [0], [0, 1, 2, 3]),
        ([3, 2, None, 1], [6, 5, None, 4], [1, 2, 3, 4, 5, 6]),  # both left chains
        ([1], [1], [1, 1]),
        ([1], [], [1]),
        ([], [2, 1, 3], [1, 2, 3]),
        ([], [], []),
    ],
)
def test_merge_bsts(a, b, expected):
    assert merge_bsts(build(a), build(b)) == expected
