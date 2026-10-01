import pytest
from helpers import load

MyHashMap = load("hashing.20_internal_hashmap").MyHashMap


def test_hashmap_put_get_overwrite():
    m = MyHashMap()
    assert m.put("a", 1) is None
    assert m.put("b", 2) is None
    assert m.put("a", 3) == 1  # returns previous value
    assert (m.get("a"), m.get("b"), m.get("z")) == (3, 2, None)
    assert len(m) == 2
    assert m.contains_key("b") and not m.contains_key("z")


def test_hashmap_remove():
    m = MyHashMap()
    m.put(1, "one")
    m.put(2, "two")
    assert m.remove(1) == "one"
    assert m.remove(1) is None
    assert m.get(1) is None and not m.contains_key(1)
    assert m.get(2) == "two"
    assert len(m) == 1


def test_hashmap_colliding_keys():
    m = MyHashMap(capacity=4)
    for key in (0, 4, 8):  # same bucket while capacity is 4
        m.put(key, key * 10)
    assert [m.get(k) for k in (0, 4, 8)] == [0, 40, 80]
    assert m.remove(4) == 40
    assert [m.get(k) for k in (0, 4, 8)] == [0, None, 80]


@pytest.mark.parametrize(
    "inserts, expected_capacity",
    [
        (0, 16),
        (12, 16),  # 12 == 16 * 0.75: not over threshold yet
        (13, 32),
        (24, 32),
        (25, 64),
    ],
)
def test_hashmap_resizes_past_threshold(inserts, expected_capacity):
    m = MyHashMap()
    for key in range(inserts):
        m.put(key, str(key))
    assert m.capacity() == expected_capacity
    assert len(m) == inserts
    assert all(m.get(key) == str(key) for key in range(inserts))


def test_hashmap_custom_load_factor_and_no_shrink():
    m = MyHashMap(capacity=2, load_factor=1.0)
    m.put("x", 1)
    m.put("y", 2)
    assert m.capacity() == 2
    m.put("y", 5)  # overwrite does not grow
    assert m.capacity() == 2
    m.put("z", 3)
    assert m.capacity() == 4
    for key in ("x", "y", "z"):
        m.remove(key)
    assert m.capacity() == 4
    assert len(m) == 0


def test_hashmap_none_key_and_tuple_keys():
    m = MyHashMap()
    m.put(None, "null")
    m.put((1, 2), "pair")
    assert m.get(None) == "null"
    assert m.get((1, 2)) == "pair"
