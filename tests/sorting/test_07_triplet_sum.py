import pytest
from helpers import load

has_triplet_sum = load("sorting.07_triplet_sum").has_triplet_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 4, 45, 6, 10, 8], 22, True),
        ([1, 2, 4, 3, 6, 7], 10, True),
        ([40, 20, 10, 3, 6, 7], 24, False),
        ([-1, 0, 1, 2], 0, True),
        ([1, 1, 1], 3, True),
        ([5, 0, 1], 15, False),  # cannot reuse 5 three times
        ([1, 1], 2, False),
        ([], 0, False),
    ],
)
def test_has_triplet_sum(arr, target, expected):
    assert has_triplet_sum(arr, target) is expected
