import pytest
from helpers import load

third_largest = load("arrays.02_third_largest").third_largest


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 14, 2, 16, 10, 20], 14),
        ([19, -10, 20, 14, 2, 16, 10], 16),
        ([2, 4, 1, 3, 5], 3),
        ([10, 2], -1),
        ([], -1),
        ([3, 1, 2], 1),
        ([-5, -1, -3, -2], -3),
    ],
)
def test_third_largest(arr, expected):
    assert third_largest(arr) == expected
