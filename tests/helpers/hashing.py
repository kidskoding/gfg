"""Test-only helpers for building and inspecting linked lists."""

from hashing import ListNode


def build_list(values):
    """Python list -> singly linked list head (None if empty)."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head):
    """Inverse of build_list(): linked list -> Python list."""
    out = []
    while head is not None:
        out.append(head.value)
        head = head.next
    return out
