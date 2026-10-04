import pytest
from helpers import load

ternary_search = load("10_searching.30_ternary_search").ternary_search

TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.mark.parametrize(
    "arr, key, expected",
    [
        (TEN, 5, 4),
        (TEN, 50, -1),
        (TEN, 1, 0),
        (TEN, 10, 9),
        ([-5, -2, 0, 7], -2, 1),
        ([-5, -2, 0, 7], 1, -1),
        ([4], 4, 0),
        ([], 3, -1),
    ],
)
def test_ternary_search(arr, key, expected):
    assert ternary_search(arr, key) == expected
