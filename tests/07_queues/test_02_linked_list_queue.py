import pytest
from helpers import load

LinkedQueue = load("07_queues.02_linked_list_queue").LinkedQueue


def _run(ops):
    q = LinkedQueue()
    return [getattr(q, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("enqueue", 10),
                ("enqueue", 20),
                ("dequeue",),
                ("dequeue",),
                ("enqueue", 30),
                ("enqueue", 40),
                ("enqueue", 50),
                ("dequeue",),
                ("front",),
                ("rear",),
            ],
            [None, None, 10, 20, None, None, None, 30, 40, 50],
        ),
        (
            [("is_empty",), ("dequeue",), ("front",), ("rear",), ("__len__",)],
            [True, None, None, None, 0],
        ),
        (
            [
                ("enqueue", 1),
                ("front",),
                ("rear",),
                ("dequeue",),
                ("is_empty",),
                ("rear",),
                ("enqueue", 2),
                ("front",),
                ("rear",),
            ],
            [None, 1, 1, 1, True, None, None, 2, 2],
        ),
        (
            [
                ("enqueue", "x"),
                ("enqueue", "x"),
                ("enqueue", "y"),
                ("__len__",),
                ("dequeue",),
                ("__len__",),
                ("is_empty",),
            ],
            [None, None, None, 3, "x", 2, False],
        ),
        (
            [
                ("enqueue", -1),
                ("enqueue", 0),
                ("dequeue",),
                ("dequeue",),
                ("dequeue",),
                ("__len__",),
            ],
            [None, None, -1, 0, None, 0],
        ),
    ],
)
def test_linked_queue_ops(ops, expected):
    assert _run(ops) == expected


def test_linked_queue_fifo_order():
    q = LinkedQueue()
    for i in range(50):
        q.enqueue(i)
    assert len(q) == 50
    assert [q.dequeue() for _ in range(51)] == list(range(50)) + [None]
