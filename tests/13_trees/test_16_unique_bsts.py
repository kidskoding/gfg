import pytest
from helpers import load

count_unique_bsts = load("13_trees.16_unique_bsts").count_unique_bsts


@pytest.mark.parametrize(
    "n, expected", [(1, 1), (2, 2), (3, 5), (4, 14), (5, 42), (10, 16796), (19, 1767263190)]
)
def test_count_unique_bsts(n, expected):
    assert count_unique_bsts(n) == expected
