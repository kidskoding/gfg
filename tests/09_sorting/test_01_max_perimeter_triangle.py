import pytest
from helpers import load

max_perimeter = load("09_sorting.01_max_perimeter_triangle").max_perimeter


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([6, 1, 6, 5, 8, 4], 20),
        ([2, 3, 2, 4, 5], 12),
        ([7, 2, 3, 10, 4], 21),
        ([2, 99, 101], -1),  # 2 + 99 == 101 is degenerate
        ([1, 2, 3], -1),
        ([3, 3, 3], 9),
        ([5, 5, 5, 5], 15),
        ([1, 1], -1),
    ],
)
def test_max_perimeter(arr, expected):
    assert max_perimeter(arr) == expected
