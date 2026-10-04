import pytest
from helpers import load

interval_intersection = load(
    "01_arrays.31_interval_list_intersection"
).interval_intersection


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        ),
        ([[0, 4], [6, 10], [12, 13]], [[5, 6], [8, 13]], [[6, 6], [8, 10], [12, 13]]),
        ([[1, 3], [5, 9]], [], []),
        ([], [[1, 2]], []),
        ([[1, 7]], [[3, 10]], [[3, 7]]),
        ([[1, 2]], [[3, 4]], []),
        ([[0, 10]], [[1, 2], [4, 5], [9, 12]], [[1, 2], [4, 5], [9, 10]]),
    ],
)
def test_interval_intersection(a, b, expected):
    assert interval_intersection(a, b) == expected
