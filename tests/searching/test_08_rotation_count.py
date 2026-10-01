import pytest
from helpers import load

rotation_count = load("searching.08_rotation_count").rotation_count


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([15, 18, 2, 3, 6, 12], 2),
        ([7, 9, 11, 12, 5], 4),
        ([7, 9, 11, 12, 15], 0),  # not rotated
        ([3, 4, 5, 1, 2], 3),
        ([5, -3, -1, 0], 1),
        ([2, 1], 1),
        ([-5, -3], 0),
        ([1], 0),
    ],
)
def test_rotation_count(arr, expected):
    assert rotation_count(arr) == expected
