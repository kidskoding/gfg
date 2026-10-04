from collections import deque

import pytest
from helpers import load

interleave_halves = load("07_queues.07_interleave_queue_halves").interleave_halves


@pytest.mark.parametrize(
    "items, expected",
    [
        (
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [11, 16, 12, 17, 13, 18, 14, 19, 15, 20],
        ),
        ([1, 2, 3, 4], [1, 3, 2, 4]),
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 2, 6, 3, 7, 4, 8]),
        ([5, 5, 6, 6], [5, 6, 5, 6]),
        ([2, 1], [2, 1]),
        ([-3, 0, 3, -3, 0, 3], [-3, -3, 0, 0, 3, 3]),
        ([], []),
    ],
)
def test_interleave_halves(items, expected):
    q = deque(items)
    assert interleave_halves(q) is None
    assert list(q) == expected
