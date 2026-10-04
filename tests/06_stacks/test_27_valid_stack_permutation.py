import pytest
from helpers import load

is_stack_permutation = load("06_stacks.27_valid_stack_permutation").is_stack_permutation


@pytest.mark.parametrize(
    "pushed, popped, expected",
    [
        ([1, 2, 3], [2, 1, 3], True),
        ([1, 2, 3], [3, 1, 2], False),
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
        ([1, 2, 3], [3, 2, 1], True),
        ([1, 2], [1, 3], False),
        ([1], [1], True),
        ([], [], True),
    ],
)
def test_is_stack_permutation(pushed, popped, expected):
    assert is_stack_permutation(pushed, popped) == expected
