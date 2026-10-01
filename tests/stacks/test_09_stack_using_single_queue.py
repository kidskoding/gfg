import pytest
from helpers import load

SingleQueueStack = load("stacks.09_stack_using_single_queue").SingleQueueStack


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            (),
            [
                ("push", 1),
                ("push", 2),
                ("push", 3),
                ("top",),
                ("pop",),
                ("size",),
                ("push", 4),
                ("pop",),
                ("pop",),
                ("pop",),
                ("pop",),
                ("top",),
                ("size",),
            ],
            [None, None, None, 3, 3, 2, None, 4, 2, 1, None, None, 0],
        ),
        ((), [("size",), ("pop",), ("top",)], [0, None, None]),
        (
            (),
            [("push", 5), ("push", 5), ("pop",), ("size",), ("top",)],
            [None, None, 5, 1, 5],
        ),
        (
            (),
            [("push", -1), ("top",), ("push", 0), ("top",), ("pop",), ("top",)],
            [None, -1, None, 0, 0, -1],
        ),
    ],
)
def test_single_queue_stack(args, ops, expected):
    assert _run(SingleQueueStack(*args), ops) == expected


def test_single_queue_stack_bulk_lifo():
    s = SingleQueueStack()
    for x in range(50):
        s.push(x)
    assert s.size() == 50
    assert [s.pop() for _ in range(50)] == list(range(49, -1, -1))
    assert s.size() == 0
