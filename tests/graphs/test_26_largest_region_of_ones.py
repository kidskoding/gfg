import pytest
from helpers import load

largest_region = load("graphs.26_largest_region_of_ones").largest_region


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 0, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1]], 6),
        ([[1, 1, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1]], 5),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),  # diagonal chain
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 1),
        ([[1, 1], [1, 1]], 4),
        ([[0, 0], [0, 0]], 0),
        ([[1]], 1),
    ],
)
def test_largest_region(grid, expected):
    assert largest_region(grid) == expected
