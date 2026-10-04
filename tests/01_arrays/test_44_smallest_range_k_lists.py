import pytest
from helpers import load

smallest_range = load("01_arrays.44_smallest_range_k_lists").smallest_range


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]], [6, 8]),
        ([[2, 4], [1, 7], [20, 40]], [4, 20]),
        ([[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [2, 3, 5, 7, 11]], [1, 2]),
        ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
        ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 1]),
        ([[5, 9]], [5, 5]),
        ([[1, 10], [5, 14]], [1, 5]),
    ],
)
def test_smallest_range(lists, expected):
    assert smallest_range(lists) == expected
