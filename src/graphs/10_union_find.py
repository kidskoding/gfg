"""10. Union-Find (GFG, medium)."""


class DisjointSet:
    """Disjoint sets over elements 0..n-1."""

    def __init__(self, n: int) -> None:
        raise NotImplementedError

    def find(self, x: int) -> int:
        """Representative of x's set (same for every member of the set)."""
        raise NotImplementedError

    def union(self, x: int, y: int) -> bool:
        """Merge the sets of x and y; False if they were already the same set."""
        raise NotImplementedError

    def connected(self, x: int, y: int) -> bool:
        """True if x and y are in the same set."""
        raise NotImplementedError

    def count(self) -> int:
        """Number of disjoint sets."""
        raise NotImplementedError
