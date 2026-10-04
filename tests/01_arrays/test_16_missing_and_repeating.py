import pytest
from helpers import load

missing_and_repeating = load("01_arrays.16_missing_and_repeating").missing_and_repeating


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 2], (2, 1)),
        ([1, 3, 3], (3, 2)),
        ([4, 3, 6, 2, 1, 1], (1, 5)),
        ([1, 1], (1, 2)),
        ([3, 1, 3], (3, 2)),
        ([5, 4, 3, 2, 2], (2, 1)),
    ],
)
def test_missing_and_repeating(arr, expected):
    assert missing_and_repeating(arr) == expected
