import pytest
from helpers import load

majority_element = load("arrays.20_majority_element").majority_element


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1, 2, 1, 3, 5, 1], 1),
        ([7], 7),
        ([2, 13], -1),
        ([3, 3, 4, 4], -1),
        ([3, 1, 3, 3, 2], 3),
        ([-1, -1, 0], -1),
        ([5, 5, 5, 5], 5),
    ],
)
def test_majority_element(arr, expected):
    assert majority_element(arr) == expected
