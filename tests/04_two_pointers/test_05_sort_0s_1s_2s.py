import pytest
from helpers import load

sort012 = load("04_two_pointers.05_sort_0s_1s_2s").sort012


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2]),
        ([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]),
        ([2, 1, 0], [0, 1, 2]),
        ([2, 2, 2], [2, 2, 2]),
        ([1], [1]),
        ([], []),
    ],
)
def test_sort012(arr, expected):
    assert sort012(arr) is None
    assert arr == expected
