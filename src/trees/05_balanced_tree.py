"""05. Balanced Tree (GFG, easy)."""

from trees import TreeNode


def is_balanced(root: TreeNode | None) -> bool:
    def height(node: TreeNode | None) -> int:
        if not node:
            return -1

        return max(height(node.left), height(node.right))

    if not root or abs(height(root.left) - height(root.right)) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)


# alternative solution!
def is_balanced_alternate(root: TreeNode | None) -> bool:
    def is_balanced_alternate_helper(root: TreeNode | None) -> int:
        if not root:
            return 0

            leftHeight = is_balanced_alternate_helper(root.left)
            rightHeight = is_balanced_alternate_helper(root.right)

            if leftHeight == -1 or rightHeight == -1 or \
               abs(leftHeight - rightHeight) > 1:

                return -1

    return is_balanced_alternate_helper(root) > 0
