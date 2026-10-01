from importlib import import_module

_nodes = import_module("trees.00_tree")
TreeNode = _nodes.TreeNode

__all__ = ["TreeNode"]
