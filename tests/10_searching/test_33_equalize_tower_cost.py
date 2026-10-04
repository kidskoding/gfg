import pytest
from helpers import load

min_cost_equalize = load("10_searching.33_equalize_tower_cost").min_cost_equalize


@pytest.mark.parametrize(
    "heights, costs, expected",
    [
        ([1, 2, 3], [10, 100, 1000], 120),
        ([7, 1, 5], [1, 1, 1], 6),
        ([1, 2, 3, 4], [1, 1, 1, 1], 4),
        ([1, 10], [5, 1], 9),  # move the cheap tower
        ([3, 1, 2], [1, 1, 100], 2),
        ([4, 4, 4], [1, 2, 3], 0),
        ([5], [3], 0),
    ],
)
def test_min_cost_equalize(heights, costs, expected):
    assert min_cost_equalize(heights, costs) == expected
