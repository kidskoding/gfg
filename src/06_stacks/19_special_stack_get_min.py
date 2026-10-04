"""19. A Stack with getMin() in O(1) Time (GFG, medium)."""


class SpecialStack:
    """Stack with O(1) push/pop/peek/get_min (an auxiliary stack is allowed);
    pop, peek and get_min return None when empty."""

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
