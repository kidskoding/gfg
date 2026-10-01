"""Test-only helpers for building and inspecting linked lists (sorting topic)."""

from sorting.linked_list import ListNode

MAX_NODES = 10_000  # guard against cycles so a wrong solution fails instead of hanging


def build_list(values):
    """Python list -> singly linked list (prev left as None)."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head):
    """Singly linked list -> Python list of values."""
    out = []
    while head is not None:
        assert len(out) < MAX_NODES, "cycle detected"
        out.append(head.value)
        head = head.next
    return out


def nodes(head):
    """All nodes reachable via next, in order."""
    out = []
    while head is not None:
        assert len(out) < MAX_NODES, "cycle detected"
        out.append(head)
        head = head.next
    return out


def build_dll(values):
    """Python list -> doubly linked list with consistent prev pointers."""
    head = build_list(values)
    prev = None
    for node in nodes(head):
        node.prev = prev
        prev = node
    return head


def dll_to_list(head):
    """Doubly linked list -> Python list of values; asserts every prev pointer is consistent."""
    out, prev = [], None
    for node in nodes(head):
        assert node.prev is prev, f"bad prev pointer at {node.value!r}"
        out.append(node.value)
        prev = node
    return out
