import pytest
from helpers import load

has_pair_with_diff = load("sorting.06_pair_with_difference").has_pair_with_diff


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        ([5, 20, 3, 2, 50, 80], 78, True),
        ([90, 70, 20, 80, 50], 45, False),
        ([1, 8, 30, 40, 100], 60, True),
        ([1, 2, 3], 0, False),  # an element cannot pair with itself
        ([1, 2, 2], 0, True),
        ([5, 1], -4, True),
        ([-3, 4], 7, True),
        ([7], 0, False),
    ],
)
def test_has_pair_with_diff(arr, x, expected):
    assert has_pair_with_diff(arr, x) is expected
