import pytest
from helpers import load

dominant_pairs = load("04_two_pointers.11_dominant_pairs").dominant_pairs


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 2, 2, 1], 2),
        ([10, 8, 2, 1, 1, 2], 5),
        ([5, 1], 1),  # equality counts
        ([1, 1], 0),
        ([0, 0, 0, 0], 4),
        ([-1, -1], 1),  # -1 >= -5
        ([], 0),
    ],
)
def test_dominant_pairs(arr, expected):
    assert dominant_pairs(arr) == expected
