import pytest
from helpers import load

next_smaller_of_next_greater = load(
    "06_stacks.13_next_smaller_of_next_greater"
).next_smaller_of_next_greater


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([5, 1, 9, 2, 5, 1, 7], [2, 2, -1, 1, -1, -1, -1]),
        ([4, 8, 2, 1, 9, 5, 6, 3], [2, 5, 5, 5, -1, 3, -1, -1]),
        ([1, 3, 2], [2, -1, -1]),
        ([2, 2, 5, 1], [1, 1, -1, -1]),
        ([1, 2, 3], [-1, -1, -1]),
        ([3, 2, 1], [-1, -1, -1]),
        ([], []),
    ],
)
def test_next_smaller_of_next_greater(arr, expected):
    assert next_smaller_of_next_greater(arr) == expected
