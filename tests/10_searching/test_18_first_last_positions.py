import pytest
from helpers import load

first_last = load("10_searching.18_first_last_positions").first_last


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        ([1, 3, 5, 5, 5, 5, 67, 123, 125], 5, (2, 5)),
        ([1, 3, 5, 5, 5, 5, 7, 123, 125], 7, (6, 6)),
        ([2, 2, 2], 2, (0, 2)),
        ([1, 2, 3], 1, (0, 0)),
        ([1, 2, 3], 3, (2, 2)),
        ([1, 2, 3], 4, (-1, -1)),
        ([1], 1, (0, 0)),
        ([], 1, (-1, -1)),
    ],
)
def test_first_last(arr, x, expected):
    assert tuple(first_last(arr, x)) == expected
