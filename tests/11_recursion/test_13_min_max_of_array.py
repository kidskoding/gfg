import pytest
from helpers import load

min_max = load("11_recursion.13_min_max_of_array").min_max


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 4, 3, -5, -4, 8, 6], (-5, 8)),
        ([1, 4, 45, 6, 10, -8], (-8, 45)),
        ([7], (7, 7)),
        ([3, 3, 3], (3, 3)),
        ([2, 1], (1, 2)),
        ([-1, -9, -3], (-9, -1)),
        ([5, 4, 3, 2, 1], (1, 5)),
    ],
)
def test_min_max(arr, expected):
    assert tuple(min_max(arr)) == expected
