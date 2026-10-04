from collections import deque

import pytest
from helpers import load

reverse_queue = load("11_recursion.19_reverse_queue").reverse_queue


@pytest.mark.parametrize(
    "items, expected",
    [
        (
            [56, 27, 30, 45, 85, 92, 58, 88, 90, 10],
            [10, 90, 88, 58, 92, 85, 45, 30, 27, 56],
        ),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([7], [7]),
        ([], []),
        ([2, 2, 1, 1], [1, 1, 2, 2]),
    ],
)
def test_reverse_queue(items, expected):
    q = deque(items)
    result = reverse_queue(q)
    assert result is None
    assert list(q) == expected
