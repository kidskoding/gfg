"""11. Stack using Singly Linked List (GFG, easy)."""


class LinkedStack:
    """LIFO stack on a singly linked list; every operation O(1).
    pop/peek raise IndexError when the stack is empty."""

    def __init__(self) -> None:
        raise NotImplementedError

    def push(self, value: object) -> None:
        raise NotImplementedError

    def pop(self) -> object:
        raise NotImplementedError

    def peek(self) -> object:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
