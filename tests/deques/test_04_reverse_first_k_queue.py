from collections import deque

import pytest
from helpers import load

reverse_first_k = load("deques.04_reverse_first_k_queue").reverse_first_k


@pytest.mark.parametrize(
    "values, k, expected",
    [
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([4, 3, 2, 1], 4, [1, 2, 3, 4]),
        ([10, 20, 30, 40, 50, 60], 5, [50, 40, 30, 20, 10, 60]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([5, 5, 1, 2], 2, [5, 5, 1, 2]),  # duplicates
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3], -1, [1, 2, 3]),
        ([1, 2, 3], 5, [1, 2, 3]),  # k > size: unchanged
        ([7], 1, [7]),
        ([], 0, []),
    ],
)
def test_reverse_first_k(values, k, expected):
    queue = deque(values)
    out = reverse_first_k(queue, k)
    assert out is queue
    assert list(queue) == expected
