import pytest
from helpers import load

reverse_array = load("arrays.03_reverse_array").reverse_array


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 4, 3, 2, 6, 5], [5, 6, 2, 3, 4, 1]),
        ([4, 5, 1, 2], [2, 1, 5, 4]),
        ([1, 2, 3], [3, 2, 1]),
        ([7], [7]),
        ([], []),
        ([2, 2, -1], [-1, 2, 2]),
    ],
)
def test_reverse_array(arr, expected):
    reverse_array(arr)
    assert arr == expected
