"""03. Mirror Tree (GFG, easy)."""

from core.tree_node import TreeNode


def mirror(root: TreeNode | None) -> None:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)
