"""Test-only helpers for building and inspecting linked lists."""

from linked_lists.linked_list import DListNode, ListNode

LIMIT = 10_000  # walks stop here so a cyclic list fails a test instead of hanging


def build_list(values):
    """List of values -> singly linked list; returns the head (None if empty)."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def nodes(head, limit=LIMIT):
    """Nodes reachable via next, in order. Fails on a cycle or a list longer than limit."""
    out, seen = [], set()
    while head is not None:
        assert id(head) not in seen, "cycle detected"
        assert len(out) < limit, "list too long"
        seen.add(id(head))
        out.append(head)
        head = head.next
    return out


def to_list(head):
    """Inverse of build_list()."""
    return [node.value for node in nodes(head)]


def build_cycle(values, pos):
    """Like build_list, but the tail links back to the node at index pos (-1: no cycle).
    Returns (head, list of nodes in original order)."""
    head = build_list(values)
    all_nodes = nodes(head)
    if pos >= 0:
        all_nodes[-1].next = all_nodes[pos]
    return head, all_nodes


def build_circular(values):
    """List of values -> circular singly linked list (tail.next is head)."""
    head = build_list(values)
    if head is not None:
        nodes(head)[-1].next = head
    return head


def circular_to_list(head, limit=LIMIT):
    """Values of a circular list starting at head. Fails unless it loops back to head."""
    out, node = [], head
    while node is not None:
        assert len(out) < limit, "did not loop back to head"
        out.append(node.value)
        node = node.next
        if node is head:
            return out
    assert head is None, "list is not circular"
    return out


def build_dlist(values):
    """List of values -> doubly linked list; returns the head (None if empty)."""
    head = prev = None
    for value in values:
        node = DListNode(value, prev=prev)
        if prev is None:
            head = node
        else:
            prev.next = node
        prev = node
    return head


def to_dlist(head, limit=LIMIT):
    """Values of a doubly linked list. Also checks head.prev is None and prev/next agree."""
    if head is None:
        return []
    assert head.prev is None, "head.prev must be None"
    out, node = [], head
    while node is not None:
        assert len(out) < limit, "list too long"
        out.append(node.value)
        if node.next is not None:
            assert node.next.prev is node, "prev/next mismatch"
        node = node.next
    return out
