import pytest
from helpers import load

total_fruits = load("sliding_window.10_fruits_two_baskets").total_fruits


@pytest.mark.parametrize(
    "fruits, expected",
    [
        ([2, 1, 2], 3),
        ([3, 1, 2, 2, 2, 2], 5),
        ([1, 2, 3, 2, 2], 4),
        ([0, 1, 2, 2], 3),
        ([1, 2, 1, 2, 1], 5),
        ([4, 4, 4], 3),
        ([5], 1),
        ([], 0),
    ],
)
def test_total_fruits(fruits, expected):
    assert total_fruits(fruits) == expected
