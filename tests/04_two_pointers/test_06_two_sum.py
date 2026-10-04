import pytest
from helpers import load

two_sum = load("04_two_pointers.06_two_sum").two_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([0, -1, 2, -3, 1], -2, True),
        ([1, -2, 1, 0, 5], 0, False),
        ([1, 4, 45, 6, 10, 8], 16, True),
        ([5, 5], 10, True),
        ([3], 6, False),  # cannot reuse the same element
        ([5], 10, False),
        ([], 0, False),
    ],
)
def test_two_sum(arr, target, expected):
    assert two_sum(arr, target) is expected
