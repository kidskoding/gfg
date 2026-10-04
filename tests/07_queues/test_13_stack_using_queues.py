import pytest
from helpers import load

QueueStack = load("07_queues.13_stack_using_queues").QueueStack


def _run(ops):
    s = QueueStack()
    return [getattr(s, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [("push", 2), ("push", 3), ("pop",), ("push", 4), ("pop",)],
            [None, None, 3, None, 4],
        ),
        (
            [
                ("push", 1),
                ("push", 2),
                ("top",),
                ("pop",),
                ("top",),
                ("pop",),
                ("pop",),
                ("is_empty",),
            ],
            [None, None, 2, 2, 1, 1, None, True],
        ),
        (
            [("is_empty",), ("pop",), ("top",), ("__len__",)],
            [True, None, None, 0],
        ),
        (
            [
                ("push", "a"),
                ("push", "a"),
                ("push", "b"),
                ("__len__",),
                ("pop",),
                ("top",),
                ("__len__",),
            ],
            [None, None, None, 3, "b", "a", 2],
        ),
        (
            [
                ("push", -1),
                ("pop",),
                ("push", 0),
                ("push", 7),
                ("pop",),
                ("pop",),
                ("is_empty",),
            ],
            [None, -1, None, None, 7, 0, True],
        ),
    ],
)
def test_queue_stack_ops(ops, expected):
    assert _run(ops) == expected


def test_queue_stack_lifo_order():
    s = QueueStack()
    for i in range(40):
        s.push(i)
    assert len(s) == 40
    assert [s.pop() for _ in range(41)] == list(range(39, -1, -1)) + [None]
