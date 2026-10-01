import pytest
from helpers import load

next_greater_frequency = load("stacks.23_next_greater_frequency").next_greater_frequency


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 1, 2, 3, 4, 2, 1], [-1, -1, 1, 2, 2, 1, -1]),
        ([1, 1, 1, 2, 2, 2, 2, 11, 3, 3], [2, 2, 2, -1, -1, -1, -1, 3, -1, -1]),
        ([3, 1, 1], [1, -1, -1]),
        ([1, 2, 3], [-1, -1, -1]),
        ([5], [-1]),
        ([], []),
    ],
)
def test_next_greater_frequency(arr, expected):
    assert next_greater_frequency(arr) == expected
