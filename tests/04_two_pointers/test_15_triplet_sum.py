import pytest
from helpers import load

has_triplet_sum = load("04_two_pointers.15_triplet_sum").has_triplet_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 4, 45, 6, 10, 8], 13, True),
        ([1, 2, 4, 3, 6, 7], 10, True),
        ([40, 20, 10, 3, 6, 7], 24, False),
        ([-1, 2, -3, 5], 4, True),
        ([5, 5, 5], 15, True),
        ([5, 5], 15, False),  # cannot reuse an element
        ([0, 0, 0], 0, True),
        ([], 0, False),
    ],
)
def test_has_triplet_sum(arr, target, expected):
    assert has_triplet_sum(arr, target) is expected
