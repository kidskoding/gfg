"""16. Open Addressing for Collision Handling (GFG, medium)."""


class LinearProbingHashSet:
    """Integer key set with linear probing: probe key % capacity, +1, +2, ... (wrapping); lazy deletion."""

    def __init__(self, capacity: int) -> None:
        """Empty table with `capacity` slots (no resizing)."""
        raise NotImplementedError

    def insert(self, key: int) -> bool:
        """If absent, place key in the first empty or deleted slot on its probe path; False only if full."""
        raise NotImplementedError

    def remove(self, key: int) -> bool:
        """Mark key's slot deleted (a tombstone that probes skip over); True if it was present."""
        raise NotImplementedError

    def contains(self, key: int) -> bool:
        """True if key is in the table (probe until an empty slot or a full cycle)."""
        raise NotImplementedError

    def slots(self) -> list[int | None]:
        """Key stored in each slot; None for empty and deleted slots."""
        raise NotImplementedError
