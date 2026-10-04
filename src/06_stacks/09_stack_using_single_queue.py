"""09. Stack using single queue (GFG, medium)."""


class SingleQueueStack:
    """LIFO stack built from ONE collections.deque used as a queue (append/popleft, rotate by re-enqueuing);
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
