import pytest
from helpers import load

sort_stack = load("06_stacks.14_sort_stack_temp_stack").sort_stack


@pytest.mark.parametrize(
    "stack, expected",
    [
        ([34, 3, 31, 98, 92, 23], [3, 23, 31, 34, 92, 98]),
        ([-5, 10, -3, 0], [-5, -3, 0, 10]),
        ([3, 1, 2, 1], [1, 1, 2, 3]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
    ],
)
def test_sort_stack(stack, expected):
    assert sort_stack(list(stack)) == expected
