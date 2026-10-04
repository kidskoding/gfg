"""06. Children Sum Parent (GFG, easy)."""

from core.tree_node import TreeNode


def is_sum_property(root: TreeNode | None) -> bool:
    if (not root) or (not root.left and not root.right):
        return True

    left_val = root.left.value if root.left is not None else 0
    right_val = root.right.value if root.right is not None else 0
    if left_val + right_val != root.value:
        return False

    return is_sum_property(root.left) and is_sum_property(root.right)
