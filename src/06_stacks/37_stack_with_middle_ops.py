"""37. Stack with findMiddle() and deleteMiddle() (GFG, hard)."""


class MiddleStack:
    """Stack with O(1) push/pop/find_middle/delete_middle (doubly linked list + middle pointer).
    With n items counted from the bottom (0-based), the middle is index (n - 1) // 2.
    pop/find_middle/delete_middle return the affected value, or None when empty."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int | None:
        raise NotImplementedError

    def find_middle(self) -> int | None:
        raise NotImplementedError

    def delete_middle(self) -> int | None:
        raise NotImplementedError
