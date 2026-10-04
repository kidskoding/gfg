import pytest
from helpers import load

sort_stack = load("06_stacks.36_sort_stack_recursion").sort_stack


@pytest.mark.parametrize(
    "stack, expected",
    [
        ([-3, 14, 18, -5, 30], [-5, -3, 14, 18, 30]),
        ([3, 1, 2], [1, 2, 3]),
        ([2, 2, 1, 1], [1, 1, 2, 2]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
    ],
)
def test_sort_stack(stack, expected):
    assert sort_stack(stack) is None
    assert stack == expected
