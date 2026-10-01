import pytest
from helpers import load

smallest_range = load("hashing.19_smallest_range_k_lists").smallest_range


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]], (6, 8)),
        ([[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [2, 3, 5, 7, 11]], (1, 2)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], (3, 7)),
        ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], (20, 24)),
        ([[1, 10], [2, 11]], (1, 2)),  # tie in width: smaller lo wins
        ([[5, 9]], (5, 5)),
        ([[1], [1], [1]], (1, 1)),
        ([[-5, 0, 5], [-3, 3], [-1, 1]], (-3, 0)),
    ],
)
def test_smallest_range(lists, expected):
    assert smallest_range(lists) == expected
