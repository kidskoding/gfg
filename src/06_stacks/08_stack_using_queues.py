"""08. Stack using Queues (GFG, medium)."""


class QueueStack:
    """LIFO stack built only from two collections.deque used as queues (append/popleft);
    pop and top return None when empty."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int | None:
        raise NotImplementedError

    def top(self) -> int | None:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError
