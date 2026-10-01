import pytest
from helpers.sorting import build_dll, build_list, dll_to_list, nodes, to_list


def test_build_list_roundtrip():
    head = build_list([3, 1, 2])
    assert (head.value, head.next.value, head.next.next.value) == (3, 1, 2)
    assert head.next.next.next is None
    assert to_list(head) == [3, 1, 2]


def test_build_list_empty():
    assert build_list([]) is None
    assert to_list(None) == []
    assert nodes(None) == []


def test_build_dll_prev_pointers():
    head = build_dll([1, 2, 3])
    second, third = head.next, head.next.next
    assert head.prev is None
    assert second.prev is head
    assert third.prev is second
    assert dll_to_list(head) == [1, 2, 3]
    assert build_dll([]) is None


def test_dll_to_list_rejects_bad_prev():
    head = build_dll([1, 2, 3])
    head.next.next.prev = head
    with pytest.raises(AssertionError):
        dll_to_list(head)


def test_to_list_detects_cycle():
    head = build_list([1, 2])
    head.next.next = head
    with pytest.raises(AssertionError):
        to_list(head)
