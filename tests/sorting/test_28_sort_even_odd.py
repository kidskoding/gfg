import pytest
from helpers import load

sort_even_odd = load("sorting.28_sort_even_odd").sort_even_odd


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 5, 4, 7, 10], [7, 5, 3, 1, 2, 4, 10]),
        ([0, 4, 5, 3, 7, 2, 1], [7, 5, 3, 1, 0, 2, 4]),
        ([-3, -2, 1, 4], [1, -3, -2, 4]),
        ([6, 2, 4], [2, 4, 6]),
        ([3, 1, 5], [5, 3, 1]),
        ([], []),
    ],
)
def test_sort_even_odd(arr, expected):
    assert sort_even_odd(arr) is None
    assert arr == expected
