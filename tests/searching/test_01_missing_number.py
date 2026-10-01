import pytest
from helpers import load

missing_number = load("searching.01_missing_number").missing_number


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 5], 4),
        ([8, 2, 4, 5, 3, 7, 1], 6),
        ([2, 3, 4], 1),  # first missing
        ([1, 2, 3, 4], 5),  # last missing
        ([5, 3, 1, 2], 4),
        ([1], 2),
        ([2], 1),
        ([], 1),
    ],
)
def test_missing_number(arr, expected):
    assert missing_number(arr) == expected
