import pytest
from helpers import load

has_pair_with_sum = load("hashing.03_pair_with_given_sum").has_pair_with_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([0, -1, 2, -3, 1], -2, True),
        ([1, -2, 1, 0, 5], 0, False),
        ([1, 4, 45, 6, 10, 8], 16, True),
        ([5], 10, False),  # one element can't pair with itself
        ([5, 5], 10, True),  # two copies may pair
        ([], 0, False),
        ([3, 3, 3], 7, False),
        ([-4, -6, 2], -10, True),
    ],
)
def test_has_pair_with_sum(arr, target, expected):
    assert has_pair_with_sum(arr, target) is expected
