"""20. Internal Working of HashMap in Java (GFG, hard)."""

from collections.abc import Hashable
from typing import Any


class MyHashMap:
    """Java-style HashMap: array of chained buckets, index = hash(key) % capacity, resize by doubling."""

    def __init__(self, capacity: int = 16, load_factor: float = 0.75) -> None:
        """Empty map with `capacity` buckets."""
        raise NotImplementedError

    def put(self, key: Hashable, value: Any) -> Any | None:
        """Insert or overwrite; return the previous value (None if new). Double capacity if size > capacity * load_factor."""
        raise NotImplementedError

    def get(self, key: Hashable) -> Any | None:
        """Value for key, or None if absent."""
        raise NotImplementedError

    def remove(self, key: Hashable) -> Any | None:
        """Delete key; return its value, or None if absent. Never shrinks."""
        raise NotImplementedError

    def contains_key(self, key: Hashable) -> bool:
        """True if key is present."""
        raise NotImplementedError

    def capacity(self) -> int:
        """Current number of buckets."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Number of stored keys."""
        raise NotImplementedError
