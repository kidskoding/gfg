import pytest
from helpers import load

max_rotation_sum = load("arrays.47_max_sum_rotations").max_rotation_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([8, 3, 1, 2], 29),
        ([1, 20, 2, 10], 72),
        ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 330),
        ([3], 0),
        ([], 0),
        ([5, 5, 5], 15),
        ([-1, 2, -3], 3),
    ],
)
def test_max_rotation_sum(arr, expected):
    assert max_rotation_sum(arr) == expected
