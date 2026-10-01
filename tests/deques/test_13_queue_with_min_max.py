import random

import pytest
from helpers import load

MinMaxQueue = load("deques.13_queue_with_min_max").MinMaxQueue


def _run(ops):
    queue = MinMaxQueue()
    return [getattr(queue, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("enqueue", 3),
                ("enqueue", 1),
                ("enqueue", 4),
                ("get_min",),
                ("get_max",),
                ("dequeue",),
                ("get_min",),
                ("dequeue",),
                ("get_min",),
                ("get_max",),
                ("enqueue", 2),
                ("get_min",),
                ("get_max",),
                ("dequeue",),
                ("get_max",),
                ("size",),
            ],
            [None, None, None, 1, 4, 3, 1, 1, 4, 4, None, 2, 4, 4, 2, 1],
        ),
        (
            [("get_min",), ("get_max",), ("dequeue",), ("size",)],
            [None, None, None, 0],
        ),
        (  # duplicate minimum must survive the first dequeue
            [
                ("enqueue", 2),
                ("enqueue", 2),
                ("enqueue", 5),
                ("dequeue",),
                ("get_min",),
                ("dequeue",),
                ("get_min",),
                ("get_max",),
            ],
            [None, None, None, 2, 2, 2, 5, 5],
        ),
        (
            [
                ("enqueue", -1),
                ("enqueue", -7),
                ("get_min",),
                ("get_max",),
                ("dequeue",),
                ("get_max",),
            ],
            [None, None, -7, -1, -1, -7],
        ),
    ],
)
def test_min_max_queue(ops, expected):
    assert _run(ops) == expected


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_min_max_queue_matches_model(seed):
    rng = random.Random(seed)
    queue, model = MinMaxQueue(), []
    for _ in range(400):
        if rng.random() < 0.55:
            value = rng.randint(-5, 5)
            queue.enqueue(value)
            model.append(value)
        else:
            assert queue.dequeue() == (model.pop(0) if model else None)
        assert queue.get_min() == (min(model) if model else None)
        assert queue.get_max() == (max(model) if model else None)
        assert queue.size() == len(model)
