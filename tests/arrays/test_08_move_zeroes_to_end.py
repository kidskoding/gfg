import pytest
from helpers import load

move_zeroes = load("arrays.08_move_zeroes_to_end").move_zeroes


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 0, 4, 3, 0, 5, 0], [1, 2, 4, 3, 5, 0, 0, 0]),
        ([10, 20, 30], [10, 20, 30]),
        ([0, 0], [0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, -1, 0, -2], [-1, -2, 0, 0]),
        ([], []),
    ],
)
def test_move_zeroes(arr, expected):
    move_zeroes(arr)
    assert arr == expected
