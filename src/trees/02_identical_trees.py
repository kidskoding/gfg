"""02. Identical Trees (GFG, easy)."""

from trees import TreeNode


def is_identical(a: TreeNode | None, b: TreeNode | None) -> bool:
    if not a and not b:
        return True

    if (not a or not b) or a.value != b.value:
        return False

    return is_identical(a.left, b.left) and is_identical(a.right, b.right)
