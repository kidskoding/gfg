"""13. Implement Stack using Queues (GFG, medium)."""

from typing import Any


class QueueStack:
    """LIFO stack using only collections.deque objects as queues (append / popleft / len only)."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, value: Any) -> None:
        """Push value on top."""
        raise NotImplementedError

    def pop(self) -> Any | None:
        """Remove and return the top item, or None if the stack is empty."""
        raise NotImplementedError

    def top(self) -> Any | None:
        """Top item without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
