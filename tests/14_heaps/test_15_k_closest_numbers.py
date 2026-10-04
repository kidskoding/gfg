import pytest
from helpers import load

k_closest_numbers = load("14_heaps.15_k_closest_numbers").k_closest_numbers


@pytest.mark.parametrize(
    "arr, x, k, expected",
    [
        ([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 35, 4, [39, 30, 42, 45]),
        ([1, 3, 4, 10, 12], 4, 2, [3, 1]),  # x itself is skipped
        ([1, 2, 3, 6, 7], 4, 3, [3, 6, 2]),  # 6 and 2 tie: larger first
        ([2, 4], 3, 2, [4, 2]),
        ([10, 20, 30], 1, 2, [10, 20]),  # x left of everything
        ([10, 20, 30], 100, 2, [30, 20]),  # x right of everything
    ],
)
def test_k_closest_numbers(arr, x, k, expected):
    assert k_closest_numbers(arr, x, k) == expected
