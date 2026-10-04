import pytest
from helpers import load

reverse_stack = load("06_stacks.16_reverse_stack_recursion").reverse_stack


@pytest.mark.parametrize(
    "stack, expected",
    [
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([-1, 0, 5, 2, 9], [9, 2, 5, 0, -1]),
        ([3, 3, 1], [1, 3, 3]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ],
)
def test_reverse_stack(stack, expected):
    assert reverse_stack(stack) is None
    assert stack == expected
