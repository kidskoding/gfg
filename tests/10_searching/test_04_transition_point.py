import pytest
from helpers import load

transition_point = load("10_searching.04_transition_point").transition_point


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([0, 0, 0, 1, 1], 3),
        ([0, 0, 0, 0], -1),
        ([1, 1, 1], 0),
        ([0, 1], 1),
        ([0, 0, 0, 0, 0, 1], 5),
        ([0], -1),
        ([1], 0),
        ([], -1),
    ],
)
def test_transition_point(arr, expected):
    assert transition_point(arr) == expected
