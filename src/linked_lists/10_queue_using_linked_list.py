"""10. Queue using Linked List (GFG, easy)."""


class LinkedQueue:
    """FIFO queue on a singly linked list; every operation O(1).
    dequeue/front/rear raise IndexError when the queue is empty."""

    def __init__(self) -> None:
        raise NotImplementedError

    def enqueue(self, value: object) -> None:
        raise NotImplementedError

    def dequeue(self) -> object:
        raise NotImplementedError

    def front(self) -> object:
        raise NotImplementedError

    def rear(self) -> object:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
