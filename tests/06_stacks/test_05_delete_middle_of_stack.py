import pytest
from helpers import load

delete_middle = load("06_stacks.05_delete_middle_of_stack").delete_middle


@pytest.mark.parametrize(
    "stack, expected",
    [
        ([1, 2, 3, 4, 5], [1, 2, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [1, 2, 4, 5, 6]),
        ([10, 20, 30, 40], [10, 30, 40]),
        ([1, 2, 3], [1, 3]),
        ([1, 2], [2]),
        ([5, 5, 5, 5], [5, 5, 5]),
        ([7], []),
        ([], []),
    ],
)
def test_delete_middle(stack, expected):
    assert delete_middle(stack) is None
    assert stack == expected
