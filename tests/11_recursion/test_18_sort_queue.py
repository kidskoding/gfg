from collections import deque

import pytest
from helpers import load

sort_queue = load("11_recursion.18_sort_queue").sort_queue


@pytest.mark.parametrize(
    "items, expected",
    [
        ([10, 7, 16, 9, 20, 5], [5, 7, 9, 10, 16, 20]),
        ([0, -2, -1, 2, 3, 1], [-2, -1, 0, 1, 2, 3]),
        ([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([4], [4]),
        ([], []),
    ],
)
def test_sort_queue(items, expected):
    q = deque(items)
    result = sort_queue(q)
    assert result is None
    assert list(q) == expected
