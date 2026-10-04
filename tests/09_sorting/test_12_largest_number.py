import pytest
from helpers import load

largest_number = load("09_sorting.12_largest_number").largest_number


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([3, 30, 34, 5, 9], "9534330"),
        ([54, 546, 548, 60], "6054854654"),
        ([3, 4, 6, 5, 9], "96543"),
        ([10, 2], "210"),
        ([121, 12], "12121"),
        ([0, 0], "0"),
        ([0], "0"),
    ],
)
def test_largest_number(arr, expected):
    assert largest_number(arr) == expected
