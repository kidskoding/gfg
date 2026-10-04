import pytest
from helpers import load

next_greater = load("06_stacks.11_next_greater_element").next_greater


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 3, 2, 4], [3, 4, 4, -1]),
        ([6, 8, 0, 1, 3], [8, -1, 1, 3, -1]),
        ([10, 20, 30, 50], [20, 30, 50, -1]),
        ([50, 40, 30, 10], [-1, -1, -1, -1]),
        ([4, -2, -1, 5], [5, -1, 5, -1]),
        ([5, 5, 5], [-1, -1, -1]),
        ([7], [-1]),
        ([], []),
    ],
)
def test_next_greater(arr, expected):
    assert next_greater(arr) == expected
