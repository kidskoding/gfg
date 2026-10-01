import pytest
from helpers import load

can_sort_with_stack = load("queues.08_queue_sortable_with_stack").can_sort_with_stack


@pytest.mark.parametrize(
    "q, expected",
    [
        ([5, 1, 2, 3, 4], True),
        ([5, 1, 2, 6, 3, 4], False),
        ([1, 2, 3], True),
        ([3, 2, 1], True),
        ([3, 1, 2], True),
        ([2, 3, 1], False),
        ([2, 4, 1, 3], False),
        ([4, 1, 3, 2, 6, 5], True),
        ([1], True),
        ([], True),
    ],
)
def test_can_sort_with_stack(q, expected):
    assert can_sort_with_stack(q) is expected
