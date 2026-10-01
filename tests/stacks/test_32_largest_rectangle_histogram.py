import pytest
from helpers import load

largest_rectangle = load("stacks.32_largest_rectangle_histogram").largest_rectangle


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([6, 2, 5, 4, 5, 1, 6], 12),
        ([2, 1, 5, 6, 2, 3], 10),
        ([1, 2, 3, 4, 5], 9),
        ([3, 3, 3], 9),
        ([2, 4], 4),
        ([0, 0], 0),
        ([5], 5),
        ([], 0),
    ],
)
def test_largest_rectangle(heights, expected):
    assert largest_rectangle(heights) == expected
