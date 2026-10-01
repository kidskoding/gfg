import pytest
from helpers import load

min_cost_ropes = load("greedy.13_connect_ropes_min_cost").min_cost_ropes


@pytest.mark.parametrize(
    "lengths, expected",
    [
        ([4, 3, 2, 6], 29),
        ([4, 2, 7, 6, 9], 62),
        ([1, 2, 3, 4, 5], 33),
        ([5, 5, 5, 5], 40),
        ([1, 1], 2),
        ([10], 0),
        ([], 0),
    ],
)
def test_min_cost_ropes(lengths, expected):
    assert min_cost_ropes(list(lengths)) == expected
