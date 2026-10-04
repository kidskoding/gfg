import pytest
from helpers import load

move_zeros_to_end = load("04_two_pointers.02_move_zeros_to_end").move_zeros_to_end


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 0, 4, 3, 0, 5, 0], [1, 2, 4, 3, 5, 0, 0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([10, 20, 30], [10, 20, 30]),
        ([-1, 0, -2, 0, 0, 7], [-1, -2, 7, 0, 0, 0]),
        ([0, 0], [0, 0]),
        ([0], [0]),
        ([], []),
    ],
)
def test_move_zeros_to_end(arr, expected):
    assert move_zeros_to_end(arr) is None
    assert arr == expected
