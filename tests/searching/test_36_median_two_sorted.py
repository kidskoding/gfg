import pytest
from helpers import load

median_sorted_arrays = load("searching.36_median_two_sorted").median_sorted_arrays


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10], 3.0),
        ([2, 3, 5, 8], [10, 12, 14, 16, 18, 20], 11.0),
        ([1, 2], [3, 4], 2.5),
        ([1, 3], [2], 2.0),
        ([1, 1], [1, 1], 1.0),
        ([0, 0], [-1], 0.0),
        ([], [1], 1.0),
        ([5], [], 5.0),
    ],
)
def test_median_sorted_arrays(a, b, expected):
    assert median_sorted_arrays(a, b) == pytest.approx(expected)
