from importlib import import_module

_nodes = import_module("heaps.00_list_node")
ListNode = _nodes.ListNode

__all__ = ["ListNode"]
