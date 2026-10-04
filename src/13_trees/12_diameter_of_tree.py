"""12. Diameter of Tree (GFG, medium)."""

from core.tree_node import TreeNode


def diameter(root: TreeNode | None) -> int:
    if not root:
        return 0

    def height(node: TreeNode | None) -> int:
        if not node:
            return -1

        return 1 + max(height(node.left), height(node.right))

    lheight = height(root.left)
    rheight = height(root.left)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight, ldiameter, rdiameter)
