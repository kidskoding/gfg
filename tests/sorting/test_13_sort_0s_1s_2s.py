import pytest
from helpers import load

sort012 = load("sorting.13_sort_0s_1s_2s").sort012


@pytest.mark.parametrize(
    "arr",
    [
        [0, 1, 2, 0, 1, 2],
        [2, 0, 1],
        [2, 2, 1, 1, 0, 0],
        [0, 0, 0],
        [2, 1],
        [1],
        [],
    ],
)
def test_sort012(arr):
    expected = sorted(arr)
    assert sort012(arr) is None
    assert arr == expected
