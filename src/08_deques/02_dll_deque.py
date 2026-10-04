"""02. Implementation of Deque using Doubly Linked List (GFG)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(eq=False)
class DLLNode:
    value: Any
    prev: DLLNode | None = None
    next: DLLNode | None = None


class LinkedDeque:
    """Unbounded deque built from DLLNode links (no collections.deque or list storage)."""

    def __init__(self) -> None:
        """Create an empty deque."""
        raise NotImplementedError

    def push_front(self, value: Any) -> None:
        """Add value at the front."""
        raise NotImplementedError

    def push_back(self, value: Any) -> None:
        """Add value at the back."""
        raise NotImplementedError

    def pop_front(self) -> Any | None:
        """Remove and return the front item, or None if empty."""
        raise NotImplementedError

    def pop_back(self) -> Any | None:
        """Remove and return the back item, or None if empty."""
        raise NotImplementedError

    def front(self) -> Any | None:
        """Return the front item without removing it, or None if empty."""
        raise NotImplementedError

    def back(self) -> Any | None:
        """Return the back item without removing it, or None if empty."""
        raise NotImplementedError

    def size(self) -> int:
        """Number of items currently stored."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """True when the deque holds no items."""
        raise NotImplementedError

    def clear(self) -> None:
        """Remove every item."""
        raise NotImplementedError
