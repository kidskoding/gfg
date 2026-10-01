"""38. Number of Turns in a Binary Tree (GFG, hard)."""

from trees.tree import TreeNode


def count_turns(root: TreeNode | None, a: int, b: int) -> int:
    """Direction changes on the path between the nodes holding a and b.
    Passing through the LCA from one child to the other counts as a turn.
    -1 if there is no turn."""
    raise NotImplementedError
