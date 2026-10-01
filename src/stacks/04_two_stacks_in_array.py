"""04. Two stacks in an array (GFG, easy)."""


class TwoStacks:
    """Two stacks sharing one fixed array of `capacity` slots (stack 1 grows from the left, stack 2 from the
    right); push returns False only when all slots are used, pop returns None when that stack is empty."""

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def push1(self, x: int) -> bool:
        raise NotImplementedError

    def push2(self, x: int) -> bool:
        raise NotImplementedError

    def pop1(self) -> int | None:
        raise NotImplementedError

    def pop2(self) -> int | None:
        raise NotImplementedError
