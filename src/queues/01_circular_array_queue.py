"""01. Circular Array Implementation (GFG, easy)."""

from typing import Any


class CircularQueue:
    """Fixed-capacity FIFO queue backed by a circular array (no list.pop(0), no deque)."""

    def __init__(self, capacity: int) -> None:
        """Create an empty queue that holds at most capacity items (capacity >= 1)."""
        raise NotImplementedError

    def enqueue(self, value: Any) -> bool:
        """Append value at the rear; return False (and change nothing) if the queue is full."""
        raise NotImplementedError

    def dequeue(self) -> Any | None:
        """Remove and return the front item, or None if the queue is empty."""
        raise NotImplementedError

    def front(self) -> Any | None:
        """Front item without removing it, or None if empty."""
        raise NotImplementedError

    def rear(self) -> Any | None:
        """Most recently enqueued item still in the queue, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
