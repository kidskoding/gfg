import pytest
from helpers.linked_lists import (
    build_circular,
    build_cycle,
    build_dlist,
    build_list,
    circular_to_list,
    nodes,
    to_dlist,
    to_list,
)


def test_build_list_roundtrip():
    head = build_list([1, 2, 3])
    assert (head.value, head.next.value, head.next.next.value) == (1, 2, 3)
    assert head.next.next.next is None
    assert to_list(head) == [1, 2, 3]


def test_build_list_empty():
    assert build_list([]) is None
    assert to_list(None) == []


def test_nodes_in_order():
    head = build_list([4, 5])
    assert nodes(head) == [head, head.next]


def test_build_cycle():
    head, all_nodes = build_cycle([1, 2, 3, 4], 1)
    assert all_nodes[0] is head
    assert all_nodes[3].next is all_nodes[1]
    with pytest.raises(AssertionError):
        to_list(head)


def test_build_cycle_without_loop():
    head, all_nodes = build_cycle([1, 2], -1)
    assert to_list(head) == [1, 2]
    assert len(all_nodes) == 2


def test_circular_roundtrip():
    head = build_circular([1, 2, 3])
    assert head.next.next.next is head
    assert circular_to_list(head) == [1, 2, 3]
    assert build_circular([]) is None
    assert circular_to_list(None) == []


def test_circular_to_list_rejects_linear():
    with pytest.raises(AssertionError):
        circular_to_list(build_list([1, 2]))


def test_dlist_roundtrip():
    head = build_dlist([1, 2, 3])
    assert head.prev is None
    assert head.next.prev is head
    assert to_dlist(head) == [1, 2, 3]
    assert build_dlist([]) is None
    assert to_dlist(None) == []


def test_to_dlist_checks_prev_links():
    head = build_dlist([1, 2, 3])
    head.next.next.prev = head
    with pytest.raises(AssertionError):
        to_dlist(head)
