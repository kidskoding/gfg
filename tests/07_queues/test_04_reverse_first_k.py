from collections import deque

import pytest
from helpers import load

reverse_first_k = load("07_queues.04_reverse_first_k").reverse_first_k


@pytest.mark.parametrize(
    "items, k, expected",
    [
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        (
            [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            5,
            [50, 40, 30, 20, 10, 60, 70, 80, 90, 100],
        ),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),  # k == len: whole queue
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3], 4, [1, 2, 3]),  # k > len: unchanged
        ([-1, 5, 5, -2], 2, [5, -1, 5, -2]),
        ([], 0, []),
    ],
)
def test_reverse_first_k(items, k, expected):
    q = deque(items)
    assert reverse_first_k(q, k) is None
    assert list(q) == expected
