from collections import deque

import pytest
from helpers import load

reverse_queue = load("07_queues.09_reverse_queue_recursion").reverse_queue


@pytest.mark.parametrize(
    "items, expected",
    [
        ([56, 27, 7, 8, 22], [22, 8, 7, 27, 56]),
        ([1, 2, 3], [3, 2, 1]),
        ([4, 4, 1], [1, 4, 4]),
        ([-1, 0, 1, 2], [2, 1, 0, -1]),
        ([5], [5]),
        ([], []),
        (list(range(200)), list(range(199, -1, -1))),
    ],
)
def test_reverse_queue(items, expected):
    q = deque(items)
    assert reverse_queue(q) is None
    assert list(q) == expected
