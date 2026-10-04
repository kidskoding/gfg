import pytest
from helpers import load

StackQueue = load("07_queues.05_queue_using_two_stacks").StackQueue


def _run(ops):
    q = StackQueue()
    return [getattr(q, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("enqueue", 2),
                ("enqueue", 3),
                ("dequeue",),
                ("enqueue", 4),
                ("dequeue",),
            ],
            [None, None, 2, None, 3],
        ),
        (
            [
                ("enqueue", 1),
                ("enqueue", 2),
                ("dequeue",),
                ("enqueue", 3),
                ("enqueue", 4),
                ("dequeue",),
                ("dequeue",),
                ("peek",),
                ("dequeue",),
                ("dequeue",),
            ],
            [None, None, 1, None, None, 2, 3, 4, 4, None],
        ),
        (
            [("is_empty",), ("dequeue",), ("peek",), ("__len__",)],
            [True, None, None, 0],
        ),
        (
            [
                ("enqueue", 9),
                ("peek",),
                ("__len__",),
                ("is_empty",),
                ("dequeue",),
                ("is_empty",),
            ],
            [None, 9, 1, False, 9, True],
        ),
        (
            [
                ("enqueue", 5),
                ("enqueue", 5),
                ("dequeue",),
                ("enqueue", 6),
                ("__len__",),
                ("peek",),
            ],
            [None, None, 5, None, 2, 5],
        ),
    ],
)
def test_stack_queue_ops(ops, expected):
    assert _run(ops) == expected


def test_stack_queue_interleaved_fifo():
    q = StackQueue()
    out = []
    for i in range(30):
        q.enqueue(i)
        if i % 3 == 2:
            out.append(q.dequeue())
    while not q.is_empty():
        out.append(q.dequeue())
    assert out == list(range(30))
