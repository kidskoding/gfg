import pytest
from helpers import load

tsp = load("19_bit_manipulation.39_bitmask_dp_tsp").tsp


@pytest.mark.parametrize(
    "dist, expected",
    [
        ([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]], 80),
        ([[0, 1, 2], [1, 0, 3], [2, 3, 0]], 6),
        ([[0, 1, 10], [10, 0, 1], [1, 10, 0]], 3),  # asymmetric: direction matters
        ([[0, 5], [7, 0]], 12),
        ([[0]], 0),
    ],
)
def test_tsp(dist, expected):
    assert tsp(dist) == expected


def test_tsp_line_of_cities():
    # cities on a line at positions 0..7: best tour goes out and back, cost 2 * 7
    n = 8
    dist = [[abs(i - j) for j in range(n)] for i in range(n)]
    assert tsp(dist) == 14
