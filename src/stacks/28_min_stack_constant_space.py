"""28. Stack with getMin() in O(1) (GFG, hard)."""


class MinStack:
    """Stack of ints with O(1) push/pop/peek/get_min using O(1) extra space (no auxiliary stack: keep one
    min variable and store encoded values); pop, peek and get_min return None when empty."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int | None:
        raise NotImplementedError

    def peek(self) -> int | None:
        raise NotImplementedError

    def get_min(self) -> int | None:
        raise NotImplementedError
