"""Test-only helpers for heap problems."""

from heaps import ListNode


def build_list(values):
    """Python list -> singly linked list of ListNode; returns the head (None if empty)."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head, limit=10_000):
    """Linked list -> Python list; stops after limit nodes so a cycle cannot hang a test."""
    out = []
    while head is not None and len(out) < limit:
        out.append(head.value)
        head = head.next
    return out


def is_max_heap(arr):
    """True iff the array-form binary heap satisfies the max-heap property."""
    return all(arr[(i - 1) // 2] >= arr[i] for i in range(1, len(arr)))
