import pytest
from helpers import load

max_of_mins = load("05_sliding_window.24_max_of_min_windows").max_of_mins


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 20, 30, 50, 10, 70, 30], [70, 30, 20, 10, 10, 10, 10]),
        ([10, 20, 30], [30, 20, 10]),
        ([4, 1, 3, 2], [4, 2, 1, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([3, 3, 3], [3, 3, 3]),
        ([5], [5]),
        ([], []),
    ],
)
def test_max_of_mins(arr, expected):
    assert max_of_mins(arr) == expected
