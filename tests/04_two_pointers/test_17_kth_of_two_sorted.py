import pytest
from helpers import load

kth_element = load("04_two_pointers.17_kth_of_two_sorted").kth_element


@pytest.mark.parametrize(
    "a, b, k, expected",
    [
        ([2, 3, 6, 7, 9], [1, 4, 8, 10], 5, 6),
        ([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7, 256),
        ([1, 2], [3, 4], 4, 4),
        ([-5, 0], [-3], 2, -3),
        ([1, 1, 1], [1, 1], 4, 1),
        ([], [1, 2, 3], 2, 2),
        ([5], [], 1, 5),
    ],
)
def test_kth_element(a, b, k, expected):
    assert kth_element(a, b, k) == expected
