import pytest
from helpers import load
from helpers.linked_lists import build_cycle, nodes

remove_loop = load("linked_lists.35_remove_loop").remove_loop


@pytest.mark.parametrize(
    "values, pos",
    [
        ([1, 3, 4], 1),
        ([1, 8, 3, 4], -1),  # no loop: unchanged
        ([1, 2, 3, 4], 0),  # tail links back to head
        ([1, 2, 3, 4], 3),  # self loop at tail
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8),
        ([7, 7, 7], 1),
        ([1], 0),
        ([1], -1),
    ],
)
def test_remove_loop(values, pos):
    head, all_nodes = build_cycle(values, pos)
    remove_loop(head)
    assert nodes(head) == all_nodes
    assert all_nodes[-1].next is None


def test_remove_loop_empty():
    remove_loop(None)
