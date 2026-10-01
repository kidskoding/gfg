"""01. Height of Binary Tree (GFG, easy)."""

from trees.tree import TreeNode


def height(root: TreeNode | None) -> int:
    if not root:
        return -1

    return 1 + max(height(root.left), height(root.right))
