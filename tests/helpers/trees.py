"""Test-only helpers for building and inspecting trees."""

from collections import deque

from helpers import load
from trees.tree import TreeNode


def build(values):
    """Level-order list -> tree; None marks a missing node, whose children are omitted."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0], left=None, right=None, next_right=None, random=None)
    queue = deque([root])
    it = iter(values[1:])
    while queue:
        node = queue.popleft()
        for side in ("left", "right"):
            value = next(it, None)
            if value is not None:
                child = TreeNode(value, left=None, right=None, next_right=None, random=None)
                setattr(node, side, child)
                queue.append(child)
    return root


def to_list(root):
    """Inverse of build(): level-order list with trailing Nones stripped."""
    out = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def inorder(root):
    return inorder(root.left) + [root.value] + inorder(root.right) if root else []


def find(root, value):
    """First node (level order) holding value."""
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            continue
        if node.value == value:
            return node
        queue.append(node.left)
        queue.append(node.right)
    return None


def edge_height(root):
    return -1 if root is None else 1 + max(edge_height(root.left), edge_height(root.right))


def is_height_balanced(root):
    if root is None:
        return True
    return (
        abs(edge_height(root.left) - edge_height(root.right)) <= 1
        and is_height_balanced(root.left)
        and is_height_balanced(root.right)
    )


def build_list(values):
    ListNode = load("trees.34_sorted_list_to_bst").ListNode
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head
