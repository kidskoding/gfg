from importlib import import_module

_nodes = import_module("sorting.00_linked_list")
ListNode = _nodes.ListNode

__all__ = ["ListNode"]
