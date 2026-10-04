import pytest
from helpers import load

min_moves_equalize = load("01_arrays.36_min_moves_equalize").min_moves_equalize


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], 3),
        ([4, 3, 4], 2),
        ([5], 0),
        ([2, 2, 2], 0),
        ([1, 1, 5], 4),
        ([-1, 0, 2], 4),
    ],
)
def test_min_moves_equalize(arr, expected):
    assert min_moves_equalize(arr) == expected
