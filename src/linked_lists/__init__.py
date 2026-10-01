from importlib import import_module

_nodes = import_module("linked_lists.00_linked_list")
ListNode = _nodes.ListNode
DListNode = _nodes.DListNode

__all__ = ["DListNode", "ListNode"]
