import pytest
from helpers import load
from helpers.trees import build

min_distance = load("trees.22_min_distance_between_nodes").min_distance


@pytest.mark.parametrize(
    "a, b, expected", [(4, 5, 2), (4, 6, 4), (1, 4, 2), (2, 3, 2), (4, 4, 0), (1, 1, 0)]
)
def test_min_distance(a, b, expected):
    assert min_distance(build([1, 2, 3, 4, 5, 6, 7]), a, b) == expected
