import pytest
from helpers import load

has_pair_with_difference = load(
    "10_searching.06_pair_with_difference"
).has_pair_with_difference


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        ([5, 20, 3, 2, 50, 80], 78, True),
        ([90, 70, 20, 80, 50], 45, False),
        ([1, 8, 30, 40, 100], 60, True),
        ([-10, 20], 30, True),
        ([1, 1], 0, True),  # zero difference needs a duplicate
        ([1, 2, 3], 0, False),
        ([5], 0, False),  # an element cannot pair with itself
        ([], 1, False),
    ],
)
def test_has_pair_with_difference(arr, x, expected):
    assert has_pair_with_difference(arr, x) is expected
