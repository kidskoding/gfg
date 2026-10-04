import pytest
from helpers import load

running_medians = load("14_heaps.25_median_of_stream").running_medians


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 15, 1, 3, 2, 8], [5, 10, 5, 4, 3, 4]),
        ([1, 2, 3, 4], [1, 1.5, 2, 2.5]),
        ([-1, -2], [-1, -1.5]),
        ([2, 2, 2], [2, 2, 2]),
        ([7], [7]),
        ([], []),
    ],
)
def test_running_medians(arr, expected):
    assert running_medians(arr) == pytest.approx(expected)
