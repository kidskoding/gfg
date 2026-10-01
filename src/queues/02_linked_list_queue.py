"""02. Linked List Implementation (GFG, easy)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class Node:
    value: Any
    next: Node | None = None


class LinkedQueue:
    """Unbounded FIFO queue built from Node objects with front/rear pointers; every op O(1)."""

    def __init__(self) -> None:
        raise NotImplementedError

    def enqueue(self, value: Any) -> None:
        """Append value at the rear."""
        raise NotImplementedError

    def dequeue(self) -> Any | None:
        """Remove and return the front item, or None if the queue is empty."""
        raise NotImplementedError

    def front(self) -> Any | None:
        """Front item without removing it, or None if empty."""
        raise NotImplementedError

    def rear(self) -> Any | None:
        """Rear item without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
