import pytest
from helpers import load

max_min_height = load("10_searching.45_maximize_min_flower_height").max_min_height


@pytest.mark.parametrize(
    "heights, k, w, expected",
    [
        ([2, 3, 4, 5, 1], 2, 2, 2),
        ([5, 8], 5, 1, 9),
        ([2, 2, 2, 2, 1, 1], 2, 3, 2),
        ([3, 1, 3, 1], 2, 2, 2),
        ([1, 5, 1], 2, 1, 2),
        ([1, 5, 1], 3, 3, 4),  # window covers everything
        ([1, 1, 1], 3, 3, 4),
        ([1, 2, 3], 1, 1, 2),
        ([5], 0, 1, 5),  # no days
    ],
)
def test_max_min_height(heights, k, w, expected):
    assert max_min_height(heights, k, w) == expected
