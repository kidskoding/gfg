"""19. Boundary Traversal (GFG, medium)."""

from core.tree_node import TreeNode


def boundary(root: TreeNode | None) -> list[int]:
    """Anticlockwise boundary: root, left boundary (from root.left, prefer left
    child else right, no leaves), all leaves left to right, right boundary
    (from root.right, prefer right child else left, no leaves) bottom-up."""
    raise NotImplementedError
