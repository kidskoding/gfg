import pytest
from helpers import load

mean_of_array = load("11_recursion.03_mean_of_array").mean_of_array


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], 3.0),
        ([1, 2, 3], 2.0),
        ([10, 20], 15.0),
        ([7], 7.0),
        ([1, 2], 1.5),
        ([-4, 4, -2, 2], 0.0),
        ([5, 5, 5, 5], 5.0),
        ([1.5, 2.5, 3.5], 2.5),
    ],
)
def test_mean_of_array(arr, expected):
    assert mean_of_array(arr) == pytest.approx(expected)
