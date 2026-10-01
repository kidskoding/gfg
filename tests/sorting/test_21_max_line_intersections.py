import pytest
from helpers import load

max_intersections = load("sorting.21_max_line_intersections").max_intersections


@pytest.mark.parametrize(
    "lines, expected",
    [
        ([[1, 3], [2, 3], [1, 2], [4, 4]], 3),
        ([[1, 3], [5, 6], [3, 4]], 2),  # endpoints count
        ([[1, 2], [3, 4]], 1),
        ([[-5, 5], [-3, -1], [0, 0], [0, 10]], 3),
        ([[1, 1]], 1),
        ([], 0),
    ],
)
def test_max_intersections(lines, expected):
    assert max_intersections(lines) == expected
