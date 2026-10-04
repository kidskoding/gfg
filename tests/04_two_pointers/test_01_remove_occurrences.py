import pytest
from helpers import load

remove_element = load("04_two_pointers.01_remove_occurrences").remove_element


@pytest.mark.parametrize(
    "arr, ele, expected",
    [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 3, 0, 2, 2, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([9, 9, 9], 9, []),
        ([1, 2, 3], 5, [1, 2, 3]),
        ([-1, 2, -1, 3], -1, [2, 3]),
        ([4], 4, []),
        ([], 1, []),
    ],
)
def test_remove_element(arr, ele, expected):
    k = remove_element(arr, ele)
    assert k == len(expected)
    assert arr[:k] == expected
