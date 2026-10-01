"""13. Queue with Minimum (GFG)."""

from typing import Any


class MinMaxQueue:
    """FIFO queue whose get_min / get_max run in amortized O(1)."""

    def __init__(self) -> None:
        """Create an empty queue."""
        raise NotImplementedError

    def enqueue(self, value: Any) -> None:
        """Add value at the rear."""
        raise NotImplementedError

    def dequeue(self) -> Any | None:
        """Remove and return the front item, or None if empty."""
        raise NotImplementedError

    def get_min(self) -> Any | None:
        """Smallest item currently in the queue, or None if empty."""
        raise NotImplementedError

    def get_max(self) -> Any | None:
        """Largest item currently in the queue, or None if empty."""
        raise NotImplementedError

    def size(self) -> int:
        """Number of items currently stored."""
        raise NotImplementedError
