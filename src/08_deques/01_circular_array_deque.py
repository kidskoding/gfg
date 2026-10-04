"""01. Circular Array Implementation of Deque (GFG)."""

from typing import Any


class CircularDeque:
    """Fixed-capacity deque backed by a circular array (no collections.deque)."""

    def __init__(self, capacity: int) -> None:
        """Create an empty deque that holds at most capacity items."""
        raise NotImplementedError

    def insert_front(self, value: Any) -> bool:
        """Add value at the front; return False (and change nothing) if full."""
        raise NotImplementedError

    def insert_rear(self, value: Any) -> bool:
        """Add value at the rear; return False (and change nothing) if full."""
        raise NotImplementedError

    def delete_front(self) -> Any | None:
        """Remove and return the front item, or None if empty."""
        raise NotImplementedError

    def delete_rear(self) -> Any | None:
        """Remove and return the rear item, or None if empty."""
        raise NotImplementedError

    def get_front(self) -> Any | None:
        """Return the front item without removing it, or None if empty."""
        raise NotImplementedError

    def get_rear(self) -> Any | None:
        """Return the rear item without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """True when the deque holds no items."""
        raise NotImplementedError

    def is_full(self) -> bool:
        """True when the deque holds capacity items."""
        raise NotImplementedError

    def size(self) -> int:
        """Number of items currently stored."""
        raise NotImplementedError
