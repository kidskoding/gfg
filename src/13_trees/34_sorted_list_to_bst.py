"""34. Sorted Linked List to BST (GFG, hard)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from core.tree_node import TreeNode


@dataclass(eq=False)
class ListNode:
    value: Any
    next: ListNode | None = None


def sorted_list_to_bst(head: ListNode | None) -> TreeNode | None:
    """Height-balanced BST from a sorted singly linked list."""
    raise NotImplementedError
