"""07. Queue using Stacks (GFG, medium)."""


class StackQueue:
    """FIFO queue built only from two Python lists used as stacks (append/pop from the end);
    dequeue returns None when empty."""

    def __init__(self) -> None:
        raise NotImplementedError

    def enqueue(self, x: int) -> None:
        raise NotImplementedError

    def dequeue(self) -> int | None:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError
