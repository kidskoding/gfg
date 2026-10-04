"""31. k stacks in a single array (GFG, hard)."""


class KStacks:
    """k stacks (numbered 0..k-1) sharing one array of n slots, any stack may use any free slot;
    push returns False only when all n slots are used, pop returns None when that stack is empty."""

    def __init__(self, k: int, n: int) -> None:
        raise NotImplementedError

    def push(self, x: int, sn: int) -> bool:
        raise NotImplementedError

    def pop(self, sn: int) -> int | None:
        raise NotImplementedError

    def is_empty(self, sn: int) -> bool:
        raise NotImplementedError
