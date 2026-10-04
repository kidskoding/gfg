import pytest
from helpers import load

DisjointSet = load("16_graphs.10_union_find").DisjointSet


def test_union_find_sequence():
    ds = DisjointSet(5)
    assert ds.count() == 5
    assert ds.connected(0, 1) is False
    assert ds.union(0, 1) is True
    assert ds.union(1, 0) is False
    assert ds.connected(1, 0) is True
    assert ds.union(2, 3) is True
    assert ds.count() == 3
    assert ds.union(1, 3) is True
    assert ds.connected(0, 2) is True
    assert ds.count() == 2
    assert ds.connected(0, 4) is False
    assert ds.union(4, 4) is False
    assert ds.count() == 2


def test_find_is_consistent_representative():
    ds = DisjointSet(6)
    for x, y in [(0, 1), (2, 3), (1, 3), (4, 5)]:
        ds.union(x, y)
    groups = [{0, 1, 2, 3}, {4, 5}]
    for group in groups:
        reps = {ds.find(x) for x in group}
        assert len(reps) == 1
        assert reps.pop() in group
    assert ds.find(0) != ds.find(4)


@pytest.mark.parametrize(
    "n, unions, expected_count",
    [
        (1, [], 1),
        (4, [(0, 1), (1, 2), (2, 3)], 1),
        (4, [(0, 1), (0, 1), (1, 0)], 3),
        (10, [(i, i + 1) for i in range(0, 10, 2)], 5),
        (10, [(9 - i, 9 - i - 1) for i in range(9)], 1),
    ],
)
def test_count_after_unions(n, unions, expected_count):
    ds = DisjointSet(n)
    for x, y in unions:
        ds.union(x, y)
    assert ds.count() == expected_count
    for x, y in unions:
        assert ds.connected(x, y)
