import pytest
from helpers import load

sort_stack = load("11_recursion.36_sort_stack").sort_stack


@pytest.mark.parametrize(
    "stack, expected",
    [
        ([34, 3, 31, 98, 92, 23], [3, 23, 31, 34, 92, 98]),
        ([-3, 14, 18, -5, 30], [-5, -3, 14, 18, 30]),
        ([11, 2, 32, 3, 41], [2, 3, 11, 32, 41]),
        ([3, 1, 2, 1, 3], [1, 1, 2, 3, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([7], [7]),
        ([], []),
    ],
)
def test_sort_stack(stack, expected):
    result = sort_stack(stack)
    assert result is None
    assert stack == expected  # top of stack (last element) is the greatest
