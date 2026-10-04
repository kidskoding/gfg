import pytest
from helpers import load

LinkedQueue = load("12_linked_lists.10_queue_using_linked_list").LinkedQueue


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("enqueue", 10),
                ("enqueue", 20),
                ("dequeue",),
                ("enqueue", 30),
                ("front",),
                ("rear",),
                ("len",),
            ],
            [None, None, 10, None, 20, 30, 2],
        ),
        (
            [
                ("enqueue", 2),
                ("enqueue", 3),
                ("dequeue",),
                ("enqueue", 4),
                ("dequeue",),
                ("dequeue",),
                ("empty",),
            ],
            [None, None, 2, None, 3, 4, True],
        ),
        (
            [
                ("empty",),
                ("len",),
                ("enqueue", 1),
                ("empty",),
                ("front",),
                ("rear",),
                ("len",),
            ],
            [True, 0, None, False, 1, 1, 1],
        ),
        (
            # drain to empty then refill: rear must be reset correctly
            [
                ("enqueue", 1),
                ("dequeue",),
                ("enqueue", 5),
                ("enqueue", 6),
                ("front",),
                ("rear",),
            ],
            [None, 1, None, None, 5, 6],
        ),
        (
            [("enqueue", "a"), ("enqueue", "a"), ("dequeue",), ("len",), ("rear",)],
            [None, None, "a", 1, "a"],
        ),
    ],
)
def test_linked_queue(ops, expected):
    queue = LinkedQueue()
    calls = {
        "enqueue": queue.enqueue,
        "dequeue": queue.dequeue,
        "front": queue.front,
        "rear": queue.rear,
        "empty": queue.is_empty,
        "len": lambda: len(queue),
    }
    assert [calls[name](*args) for name, *args in ops] == expected


@pytest.mark.parametrize("method", ["dequeue", "front", "rear"])
def test_linked_queue_empty_raises(method):
    queue = LinkedQueue()
    with pytest.raises(IndexError):
        getattr(queue, method)()


def test_linked_queue_raises_after_drain():
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.dequeue()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert queue.is_empty()


def test_linked_queue_many():
    queue = LinkedQueue()
    for i in range(1000):
        queue.enqueue(i)
    assert [queue.dequeue() for _ in range(1000)] == list(range(1000))
    assert len(queue) == 0
