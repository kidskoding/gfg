import pytest
from helpers import load

majority_element = load("10_searching.12_majority_element").majority_element


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1, 2, 1, 3, 5, 1], 1),
        ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4),
        ([5, 5, 5, 5], 5),
        ([7], 7),
        ([2, 13], -1),
        ([1, 2, 3], -1),
        ([2, 2, 1, 1], -1),  # exactly half is not a majority
        ([], -1),
    ],
)
def test_majority_element(arr, expected):
    assert majority_element(arr) == expected
