import pytest
from helpers import load

ChainedHashSet = load("hashing.15_separate_chaining").ChainedHashSet

GFG_KEYS = [50, 700, 76, 85, 92, 73, 101]


def test_chained_insert_builds_chains():
    table = ChainedHashSet(7)
    for key in GFG_KEYS:
        table.insert(key)
    assert table.buckets() == [[700], [50, 85, 92], [], [73, 101], [], [], [76]]
    assert all(table.contains(key) for key in GFG_KEYS)
    assert not table.contains(8)  # same slot as 50, 85, 92 but absent


def test_chained_remove_keeps_chain_order():
    table = ChainedHashSet(7)
    for key in GFG_KEYS:
        table.insert(key)
    assert table.remove(85) is True
    assert table.remove(85) is False
    assert table.buckets()[1] == [50, 92]
    table.insert(8)
    assert table.buckets()[1] == [50, 92, 8]
    assert not table.contains(85)
    assert table.contains(92)


def test_chained_duplicate_insert_is_noop():
    table = ChainedHashSet(3)
    table.insert(4)
    table.insert(4)
    table.insert(1)
    assert table.buckets() == [[], [4, 1], []]


def test_chained_buckets_is_a_copy():
    table = ChainedHashSet(2)
    table.insert(1)
    table.buckets()[1].append(99)
    assert table.buckets() == [[], [1]]
    assert not table.contains(99)


@pytest.mark.parametrize(
    "capacity, keys, expected",
    [
        (1, [3, 1, 2], [[3, 1, 2]]),  # one slot: everything chains
        (4, [0, 4, 8, 1], [[0, 4, 8], [1], [], []]),
        (5, [-1, 4, 9], [[], [], [], [], [-1, 4, 9]]),  # -1 % 5 == 4
        (3, [], [[], [], []]),
    ],
)
def test_chained_layouts(capacity, keys, expected):
    table = ChainedHashSet(capacity)
    for key in keys:
        table.insert(key)
    assert table.buckets() == expected


def test_chained_remove_from_empty():
    table = ChainedHashSet(4)
    assert table.remove(3) is False
    assert not table.contains(3)
