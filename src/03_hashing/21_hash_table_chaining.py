"""21. Hash Table with Chaining in Java (GFG, hard)."""

from collections.abc import Hashable
from typing import Any


class HashTable:
    """Separate-chaining map: index = hash(key) % num_buckets; doubles and rehashes when size / num_buckets >= 0.7."""

    def __init__(self, num_buckets: int = 10) -> None:
        """Empty table with `num_buckets` chains."""
        raise NotImplementedError

    def add(self, key: Hashable, value: Any) -> None:
        """Insert or overwrite; after inserting a new key, grow if the load factor reached 0.7."""
        raise NotImplementedError

    def get(self, key: Hashable) -> Any | None:
        """Value for key, or None if absent."""
        raise NotImplementedError

    def remove(self, key: Hashable) -> Any | None:
        """Delete key; return its value, or None if absent."""
        raise NotImplementedError

    def size(self) -> int:
        """Number of stored keys."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """True if no keys are stored."""
        raise NotImplementedError

    def num_buckets(self) -> int:
        """Current number of chains."""
        raise NotImplementedError
