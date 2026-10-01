import random

import pytest
from helpers import load

module = load("deques.03_stack_queue_via_deque")
DequeStack = module.DequeStack
DequeQueue = module.DequeQueue


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("push", 1),
                ("push", 2),
                ("peek",),
                ("pop",),
                ("pop",),
                ("pop",),
                ("is_empty",),
            ],
            [None, None, 2, 2, 1, None, True],
        ),
        ([("pop",), ("peek",), ("size",), ("is_empty",)], [None, None, 0, True]),
        (
            [
                ("push", 5),
                ("push", 5),
                ("push", 3),
                ("size",),
                ("pop",),
                ("peek",),
                ("push", 9),
                ("pop",),
            ],
            [None, None, None, 3, 3, 5, None, 9],
        ),
        ([("push", -1), ("peek",), ("size",), ("is_empty",)], [None, -1, 1, False]),
    ],
)
def test_deque_stack(ops, expected):
    assert _run(DequeStack(), ops) == expected


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("enqueue", 1),
                ("enqueue", 2),
                ("enqueue", 3),
                ("front",),
                ("dequeue",),
                ("size",),
                ("enqueue", 4),
                ("dequeue",),
                ("dequeue",),
                ("dequeue",),
                ("dequeue",),
                ("is_empty",),
            ],
            [None, None, None, 1, 1, 2, None, 2, 3, 4, None, True],
        ),
        ([("dequeue",), ("front",), ("size",), ("is_empty",)], [None, None, 0, True]),
        (
            [
                ("enqueue", 8),
                ("dequeue",),
                ("enqueue", 6),
                ("enqueue", 6),
                ("front",),
                ("size",),
            ],
            [None, 8, None, None, 6, 2],
        ),
    ],
)
def test_deque_queue(ops, expected):
    assert _run(DequeQueue(), ops) == expected


@pytest.mark.parametrize("seed", [0, 1])
def test_stack_and_queue_match_model(seed):
    rng = random.Random(seed)
    stack, queue, model_s, model_q = DequeStack(), DequeQueue(), [], []
    for step in range(300):
        if rng.random() < 0.55:
            stack.push(step)
            queue.enqueue(step)
            model_s.append(step)
            model_q.append(step)
        else:
            assert stack.pop() == (model_s.pop() if model_s else None)
            assert queue.dequeue() == (model_q.pop(0) if model_q else None)
        assert stack.peek() == (model_s[-1] if model_s else None)
        assert queue.front() == (model_q[0] if model_q else None)
        assert stack.size() == len(model_s) and queue.size() == len(model_q)
