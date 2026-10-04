import pytest
from helpers import load

count_le = load("10_searching.22_count_le_in_second").count_le


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3, 4, 7, 9], [0, 1, 2, 1, 1, 4], [4, 5, 5, 6, 6, 6]),
        ([4, 8, 7, 5, 1], [4, 48, 3, 0, 1, 1, 5], [5, 6, 6, 6, 3]),
        ([-1, 0], [0, 0, -1], [1, 3]),
        ([5], [5, 5, 5], [3]),  # equality counts
        ([1, 2], [], [0, 0]),
        ([], [1], []),
    ],
)
def test_count_le(a, b, expected):
    assert count_le(a, b) == expected
