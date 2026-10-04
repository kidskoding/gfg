import pytest
from helpers import load

CircularQueue = load("07_queues.01_circular_array_queue").CircularQueue


def _run(capacity, ops):
    q = CircularQueue(capacity)
    return [getattr(q, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "capacity, ops, expected",
    [
        (
            3,
            [
                ("enqueue", 1),
                ("enqueue", 2),
                ("enqueue", 3),
                ("enqueue", 4),
                ("is_full",),
                ("rear",),
            ],
            [True, True, True, False, True, 3],
        ),
        (
            3,
            [
                ("enqueue", 1),
                ("enqueue", 2),
                ("enqueue", 3),
                ("dequeue",),
                ("enqueue", 4),
                ("front",),
                ("rear",),
                ("__len__",),
            ],
            [True, True, True, 1, True, 2, 4, 3],
        ),
        (
            2,
            [
                ("is_empty",),
                ("is_full",),
                ("dequeue",),
                ("front",),
                ("rear",),
                ("__len__",),
            ],
            [True, False, None, None, None, 0],
        ),
        (
            1,
            [
                ("enqueue", "a"),
                ("enqueue", "b"),
                ("front",),
                ("rear",),
                ("dequeue",),
                ("dequeue",),
                ("enqueue", "b"),
                ("rear",),
            ],
            [True, False, "a", "a", "a", None, True, "b"],
        ),
        (
            3,
            [
                ("enqueue", 1),
                ("enqueue", 2),
                ("enqueue", 3),
                ("dequeue",),
                ("dequeue",),
                ("enqueue", 4),
                ("enqueue", 5),
                ("is_full",),
                ("dequeue",),
                ("dequeue",),
                ("dequeue",),
                ("dequeue",),
                ("is_empty",),
            ],
            [True, True, True, 1, 2, True, True, True, 3, 4, 5, None, True],
        ),
        (
            4,
            [
                ("enqueue", 7),
                ("enqueue", 7),
                ("dequeue",),
                ("__len__",),
                ("front",),
                ("rear",),
            ],
            [True, True, 7, 1, 7, 7],
        ),
    ],
)
def test_circular_queue_ops(capacity, ops, expected):
    assert _run(capacity, ops) == expected


def test_circular_queue_wraps_many_times():
    q = CircularQueue(2)
    for i in range(20):
        assert q.enqueue(i)
        assert q.enqueue(i + 100)
        assert q.is_full()
        assert q.dequeue() == i
        assert q.dequeue() == i + 100
        assert q.is_empty()
