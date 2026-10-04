import pytest
from helpers import load

HashTable = load("03_hashing.21_hash_table_chaining").HashTable


def test_hash_table_gfg_example():
    table = HashTable()
    table.add("this", 1)
    table.add("coder", 2)
    table.add("this", 4)
    table.add("hi", 5)
    assert table.size() == 3
    assert table.remove("this") == 4
    assert table.remove("this") is None
    assert table.size() == 2
    assert not table.is_empty()
    assert (table.get("coder"), table.get("hi"), table.get("this")) == (2, 5, None)


def test_hash_table_empty():
    table = HashTable()
    assert table.is_empty()
    assert table.size() == 0
    assert table.get("x") is None
    assert table.remove("x") is None
    assert table.num_buckets() == 10


@pytest.mark.parametrize(
    "inserts, expected_buckets",
    [
        (6, 10),
        (7, 20),  # 7 / 10 >= 0.7
        (13, 20),
        (14, 40),  # 14 / 20 >= 0.7
    ],
)
def test_hash_table_grows_at_load_factor(inserts, expected_buckets):
    table = HashTable()
    for key in range(inserts):
        table.add(key, key * key)
    assert table.num_buckets() == expected_buckets
    assert table.size() == inserts
    assert all(table.get(key) == key * key for key in range(inserts))


def test_hash_table_overwrite_does_not_grow():
    table = HashTable(num_buckets=2)
    table.add("a", 1)
    assert table.num_buckets() == 2  # 1 / 2 < 0.7
    for _ in range(5):
        table.add("a", 2)
    assert table.num_buckets() == 2
    assert table.size() == 1
    assert table.get("a") == 2


def test_hash_table_colliding_keys():
    table = HashTable(num_buckets=100)
    for key in (3, 103, 203):  # same chain
        table.add(key, str(key))
    assert table.remove(103) == "103"
    assert (table.get(3), table.get(103), table.get(203)) == ("3", None, "203")
    assert table.size() == 2
