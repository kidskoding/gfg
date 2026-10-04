"""05. Implement Queue using Two Stacks (GFG, easy)."""

from typing import Any


class StackQueue:
    """FIFO queue using only two Python lists as stacks (append / pop() from the end only)."""

    def __init__(self) -> None:
        raise NotImplementedError

    def enqueue(self, value: Any) -> None:
        """Append value at the rear."""
        raise NotImplementedError

    def dequeue(self) -> Any | None:
        """Remove and return the front item, or None if the queue is empty."""
        raise NotImplementedError

    def peek(self) -> Any | None:
        """Front item without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
