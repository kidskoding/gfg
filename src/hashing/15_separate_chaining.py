"""15. Separate Chaining for Collision Handling (GFG, medium)."""


class ChainedHashSet:
    """Integer key set: slot = key % capacity, each slot a chain (list) of keys in insertion order."""

    def __init__(self, capacity: int) -> None:
        """Empty table with `capacity` slots (no resizing)."""
        raise NotImplementedError

    def insert(self, key: int) -> None:
        """Append key to the end of its slot's chain; no-op if already present."""
        raise NotImplementedError

    def remove(self, key: int) -> bool:
        """Remove key from its chain (others keep their order); True if it was present."""
        raise NotImplementedError

    def contains(self, key: int) -> bool:
        """True if key is in the table."""
        raise NotImplementedError

    def buckets(self) -> list[list[int]]:
        """Copy of every chain, indexed by slot."""
        raise NotImplementedError
