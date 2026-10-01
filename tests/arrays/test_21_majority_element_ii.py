import pytest
from helpers import load

majority_element_ii = load("arrays.21_majority_element_ii").majority_element_ii


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 2, 3, 1, 3, 2, 1, 1], [1, 2]),
        ([-5, 3, -5], [-5]),
        ([3, 2, 2, 4, 1, 4], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([4, 4, 4, 4], [4]),
        ([1, 2, 3, 1, 2, 3], []),
        ([], []),
    ],
)
def test_majority_element_ii(arr, expected):
    assert majority_element_ii(arr) == expected
