"""04. Symmetric Tree (GFG, easy)."""
from trees.tree import TreeNode


def is_symmetric(root: TreeNode | None) -> bool:
    if not root:
        return True

    def is_symmetric_helper(left: TreeNode | None, right: TreeNode | None):
        if not left and not right:
            return True

        if not left or not right or left.value != right.value:
            return False

        return is_symmetric_helper(left.left, right.right) and \
            is_symmetric_helper(left.right, right.left)

    return is_symmetric_helper(root.left, root.right)
