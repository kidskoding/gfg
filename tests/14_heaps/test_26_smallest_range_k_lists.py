import pytest
from helpers import load

smallest_range = load("14_heaps.26_smallest_range_k_lists").smallest_range


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]], (6, 8)),
        ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], (20, 24)),
        ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], (1, 1)),
        ([[1, 5], [2, 6]], (1, 2)),  # (5, 6) is as narrow: smaller start wins
        ([[1], [5]], (1, 5)),
        ([[10]], (10, 10)),
    ],
)
def test_smallest_range(lists, expected):
    assert tuple(smallest_range(lists)) == expected
