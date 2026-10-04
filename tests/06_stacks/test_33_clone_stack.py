import pytest
from helpers import load

clone_stack = load("06_stacks.33_clone_stack").clone_stack


@pytest.mark.parametrize(
    "stack",
    [
        [1, 2, 3, 4],
        [3, 1, 3, 2],
        [-1, 0, 1],
        [7],
        [],
    ],
)
def test_clone_stack(stack):
    original = list(stack)
    clone = clone_stack(stack)
    assert clone == original
    assert clone is not stack
    assert stack == original
