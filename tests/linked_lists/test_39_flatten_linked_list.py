from itertools import pairwise

import pytest
from helpers import load
from helpers.linked_lists import LIMIT

from linked_lists import ListNode

flatten = load("linked_lists.39_flatten_linked_list").flatten


def _build(columns):
    """Each inner list becomes a sub-list linked by down; sub-list heads are linked by next."""
    heads = []
    for column in columns:
        head = None
        for value in reversed(column):
            head = ListNode(value, down=head)
        heads.append(head)
    for a, b in pairwise(heads):
        a.next = b
    return heads[0] if heads else None


def _down_nodes(head):
    out = []
    while head is not None:
        assert len(out) < LIMIT, "list too long"
        out.append(head)
        head = head.down
    return out


def _all_nodes(columns_head):
    out, column = [], columns_head
    while column is not None:
        out.extend(_down_nodes(column))
        column = column.next
    return out


@pytest.mark.parametrize(
    "columns",
    [
        [[5, 7, 8, 30], [10, 20], [19, 22, 50], [28, 35, 40, 45]],
        [[5, 7, 8, 30], [10, 20], [19, 22, 50], [28]],
        [[1, 2, 3]],
        [[1], [2], [3]],
        [[1, 1], [1, 2], [2, 2]],
        [[-4, 10], [-1, 0, 11]],
    ],
)
def test_flatten(columns):
    head = _build(columns)
    originals = {id(node) for node in _all_nodes(head)}
    flat = _down_nodes(flatten(head))
    assert [node.value for node in flat] == sorted(
        v for column in columns for v in column
    )
    assert {id(node) for node in flat} == originals


def test_flatten_empty():
    assert flatten(None) is None
