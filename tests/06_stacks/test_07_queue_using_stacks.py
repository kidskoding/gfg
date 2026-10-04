import pytest
from helpers import load

StackQueue = load("06_stacks.07_queue_using_stacks").StackQueue


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            (),
            [
                ("enqueue", 1),
                ("enqueue", 2),
                ("enqueue", 3),
                ("dequeue",),
                ("enqueue", 4),
                ("dequeue",),
                ("dequeue",),
                ("dequeue",),
                ("dequeue",),
                ("is_empty",),
            ],
            [None, None, None, 1, None, 2, 3, 4, None, True],
        ),
        (
            (),
            [
                ("is_empty",),
                ("dequeue",),
                ("enqueue", 5),
                ("is_empty",),
                ("dequeue",),
                ("is_empty",),
            ],
            [True, None, None, False, 5, True],
        ),
        (
            (),
            [
                ("enqueue", 1),
                ("dequeue",),
                ("enqueue", 2),
                ("enqueue", 3),
                ("dequeue",),
                ("enqueue", 4),
                ("dequeue",),
                ("dequeue",),
            ],
            [None, 1, None, None, 2, None, 3, 4],
        ),
        (
            (),
            [("enqueue", 9), ("enqueue", 9), ("dequeue",), ("dequeue",), ("dequeue",)],
            [None, None, 9, 9, None],
        ),
    ],
)
def test_stack_queue(args, ops, expected):
    assert _run(StackQueue(*args), ops) == expected


def test_stack_queue_bulk_fifo():
    q = StackQueue()
    for x in range(100):
        q.enqueue(x)
    assert [q.dequeue() for _ in range(100)] == list(range(100))
    assert q.is_empty()
