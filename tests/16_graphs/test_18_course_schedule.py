import pytest
from helpers import load

find_order = load("16_graphs.18_course_schedule").find_order


@pytest.mark.parametrize(
    "n, prerequisites",
    [
        (4, [(1, 0), (2, 0), (3, 1), (3, 2)]),
        (2, [(1, 0)]),
        (5, [(1, 0), (2, 0), (3, 1), (3, 2), (4, 3)]),
        (3, [(0, 2), (1, 2)]),
        (3, []),
        (1, []),
    ],
)
def test_find_order_is_valid(n, prerequisites):
    order = find_order(n, prerequisites)
    assert sorted(order) == list(range(n))
    pos = {v: i for i, v in enumerate(order)}
    assert all(pos[b] < pos[a] for a, b in prerequisites)


@pytest.mark.parametrize(
    "n, prerequisites",
    [
        (2, [(1, 0), (0, 1)]),
        (4, [(1, 0), (2, 1), (3, 2), (1, 3)]),
        (2, [(0, 0)]),
    ],
)
def test_find_order_impossible(n, prerequisites):
    assert find_order(n, prerequisites) == []


def test_find_order_unique():
    assert find_order(3, [(1, 0), (2, 1)]) == [0, 1, 2]
