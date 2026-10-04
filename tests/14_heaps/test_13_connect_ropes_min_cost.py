import pytest
from helpers import load

connect_ropes = load("14_heaps.13_connect_ropes_min_cost").connect_ropes


@pytest.mark.parametrize(
    "ropes, expected",
    [
        ([4, 3, 2, 6], 29),
        ([4, 2, 7, 6, 9], 62),
        ([5, 5, 5, 5], 40),
        ([1, 1], 2),
        ([10], 0),
        ([], 0),
    ],
)
def test_connect_ropes(ropes, expected):
    assert connect_ropes(ropes) == expected
