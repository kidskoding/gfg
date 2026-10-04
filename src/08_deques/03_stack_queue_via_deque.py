"""03. Stack and Queue Implementation using Deque (GFG)."""

from typing import Any


class DequeStack:
    """LIFO stack whose only storage is a collections.deque."""

    def __init__(self) -> None:
        """Create an empty stack."""
        raise NotImplementedError

    def push(self, value: Any) -> None:
        """Push value on top."""
        raise NotImplementedError

    def pop(self) -> Any | None:
        """Remove and return the top item, or None if empty."""
        raise NotImplementedError

    def peek(self) -> Any | None:
        """Return the top item without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """True when the stack holds no items."""
        raise NotImplementedError

    def size(self) -> int:
        """Number of items currently stored."""
        raise NotImplementedError


class DequeQueue:
    """FIFO queue whose only storage is a collections.deque."""

    def __init__(self) -> None:
        """Create an empty queue."""
        raise NotImplementedError

    def enqueue(self, value: Any) -> None:
        """Add value at the rear."""
        raise NotImplementedError

    def dequeue(self) -> Any | None:
        """Remove and return the front item, or None if empty."""
        raise NotImplementedError

    def front(self) -> Any | None:
        """Return the front item without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """True when the queue holds no items."""
        raise NotImplementedError

    def size(self) -> int:
        """Number of items currently stored."""
        raise NotImplementedError
