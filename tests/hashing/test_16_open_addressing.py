import pytest
from helpers import load

LinearProbingHashSet = load("hashing.16_open_addressing").LinearProbingHashSet

GFG_KEYS = [50, 700, 76, 85, 92, 73, 101]


def _gfg_table():
    table = LinearProbingHashSet(7)
    for key in GFG_KEYS:
        assert table.insert(key) is True
    return table


def test_probing_insert_layout():
    assert _gfg_table().slots() == [700, 50, 85, 92, 73, 101, 76]


def test_probing_full_table():
    table = _gfg_table()
    assert table.insert(5) is False
    assert table.insert(50) is True  # already present
    assert table.slots() == [700, 50, 85, 92, 73, 101, 76]
    assert not table.contains(5)  # full cycle, no empty slot to stop at


def test_probing_remove_leaves_tombstone():
    table = _gfg_table()
    assert table.remove(85) is True
    assert table.remove(85) is False
    assert table.slots() == [700, 50, None, 92, 73, 101, 76]
    assert table.contains(92)  # probe walks past the tombstone at slot 2
    assert table.contains(101)
    assert not table.contains(85)


def test_probing_insert_reuses_tombstone():
    table = _gfg_table()
    table.remove(85)
    assert table.insert(8) is True  # 8 % 7 == 1: slot 1 busy, slot 2 deleted
    assert table.slots() == [700, 50, 8, 92, 73, 101, 76]


def test_probing_no_duplicate_past_tombstone():
    table = LinearProbingHashSet(5)
    for key in (0, 5, 10):
        table.insert(key)
    table.remove(5)
    assert (
        table.insert(10) is True
    )  # present further along: must not be re-added at slot 1
    assert table.slots() == [0, None, 10, None, None]
    assert table.contains(10)


def test_probing_wraps_around():
    table = LinearProbingHashSet(4)
    for key in (3, 7, 11):
        table.insert(key)
    assert table.slots() == [7, 11, None, 3]
    assert table.contains(11)


@pytest.mark.parametrize("key", [0, 3, -2])
def test_probing_empty_table(key):
    table = LinearProbingHashSet(3)
    assert not table.contains(key)
    assert table.remove(key) is False
    assert table.slots() == [None, None, None]
