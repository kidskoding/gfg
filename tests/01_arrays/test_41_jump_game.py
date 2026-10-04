import pytest
from helpers import load

min_jumps = load("01_arrays.41_jump_game").min_jumps


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 3),
        ([1, 4, 3, 2, 6, 7], 2),
        ([0, 10, 20], -1),
        ([2, 3, 1, 1, 4], 2),
        ([3, 2, 1, 0, 4], -1),
        ([0], 0),
        ([1, 1, 1, 1], 3),
    ],
)
def test_min_jumps(arr, expected):
    assert min_jumps(arr) == expected
