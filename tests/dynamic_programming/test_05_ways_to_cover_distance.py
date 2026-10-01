import pytest
from helpers import load

count_ways = load("dynamic_programming.05_ways_to_cover_distance").count_ways


@pytest.mark.parametrize(
    "dist, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (5, 13),
        (10, 274),
    ],
)
def test_count_ways(dist, expected):
    assert count_ways(dist) == expected
