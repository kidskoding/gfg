"""03. Mirror Tree (GFG, easy)."""

from trees import TreeNode


def mirror(root: TreeNode | None) -> None:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)
