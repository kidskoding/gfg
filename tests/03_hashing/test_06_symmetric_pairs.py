import pytest
from helpers import load

symmetric_pairs = load("03_hashing.06_symmetric_pairs").symmetric_pairs


@pytest.mark.parametrize(
    "pairs, expected",
    [
        ([(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)], [(5, 10), (30, 40)]),
        ([(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)], [(1, 2), (4, 5)]),
        ([(1, 2), (3, 4)], []),
        ([(7, 3), (3, 7)], [(7, 3)]),  # orientation of the first occurrence
        ([(1, 2)], []),
        ([], []),
        ([(-1, 2), (2, -1), (0, 9)], [(-1, 2)]),
    ],
)
def test_symmetric_pairs(pairs, expected):
    assert sorted(symmetric_pairs(pairs)) == expected
