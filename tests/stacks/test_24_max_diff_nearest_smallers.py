import pytest
from helpers import load

max_diff_nearest_smallers = load(
    "stacks.24_max_diff_nearest_smallers"
).max_diff_nearest_smallers


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 3, 1], 1),
        ([2, 4, 8, 7, 7, 9, 3], 4),
        ([5, 1, 9, 2, 5, 1, 7], 1),
        ([1, 2, 3], 2),
        ([3, 2, 1], 2),
        ([3, 3, 3], 0),
        ([5], 0),
        ([], 0),
    ],
)
def test_max_diff_nearest_smallers(arr, expected):
    assert max_diff_nearest_smallers(arr) == expected
