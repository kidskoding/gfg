import pytest
from helpers import load

LRUCache = load("linked_lists.36_lru_cache").LRUCache


@pytest.mark.parametrize(
    "capacity, ops, expected",
    [
        (
            2,
            [
                ("put", 1, 1),
                ("put", 2, 2),
                ("get", 1),
                ("put", 3, 3),
                ("get", 2),
                ("put", 4, 4),
                ("get", 1),
                ("get", 3),
                ("get", 4),
            ],
            [None, None, 1, None, None, None, None, 3, 4],
        ),
        (
            2,
            # updating an existing key refreshes it, so 2 is evicted next
            [
                ("put", 1, 1),
                ("put", 2, 2),
                ("put", 1, 10),
                ("put", 3, 3),
                ("get", 1),
                ("get", 2),
                ("get", 3),
            ],
            [None, None, None, None, 10, None, 3],
        ),
        (
            1,
            [("put", 1, 1), ("get", 1), ("put", 2, 2), ("get", 1), ("get", 2)],
            [None, 1, None, None, 2],
        ),
        (
            3,
            # a miss does not change recency
            [
                ("put", 1, 1),
                ("put", 2, 2),
                ("put", 3, 3),
                ("get", 9),
                ("get", 1),
                ("put", 4, 4),
                ("get", 2),
                ("get", 3),
                ("get", 1),
            ],
            [None, None, None, None, 1, None, None, 3, 1],
        ),
        (
            2,
            [
                ("get", 5),
                ("put", 5, 50),
                ("put", 5, 51),
                ("put", 6, 60),
                ("get", 5),
                ("get", 6),
            ],
            [None, None, None, None, 51, 60],
        ),
    ],
)
def test_lru_cache(capacity, ops, expected):
    cache = LRUCache(capacity)
    out = [
        cache.get(op[1]) if op[0] == "get" else cache.put(op[1], op[2]) for op in ops
    ]
    assert out == expected


def test_lru_cache_many():
    cache = LRUCache(100)
    for i in range(1000):
        cache.put(i, i * i)
    assert cache.get(899) is None
    assert all(cache.get(i) == i * i for i in range(900, 1000))
