import pytest
from helpers import load

max_stack_height = load("18_dynamic_programming.19_box_stacking").max_stack_height


@pytest.mark.parametrize(
    "boxes, expected",
    [
        ([(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)], 60),
        ([(1, 2, 3)], 4),  # rotations of the same box stack
        ([(2, 2, 2)], 2),  # equal bases cannot stack
        ([(1, 1, 1), (2, 2, 2), (3, 3, 3)], 6),
        ([(1, 1, 1), (1, 1, 1)], 1),
        ([], 0),
    ],
)
def test_max_stack_height(boxes, expected):
    assert max_stack_height(boxes) == expected
