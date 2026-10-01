import pytest
from helpers import load

sort_n_squared = load("sorting.37_sort_n_squared_range").sort_n_squared


@pytest.mark.parametrize(
    "arr",
    [
        [40, 12, 45, 32, 33, 1, 22],
        [8, 5, 2, 1],
        [24, 0, 24, 13, 7],
        [3, 0, 3, 1],
        [0],
        [],
    ],
)
def test_sort_n_squared(arr):
    expected = sorted(arr)
    assert sort_n_squared(arr) is None
    assert arr == expected
