import random
from collections import deque

import pytest
from helpers import load

CircularDeque = load("deques.01_circular_array_deque").CircularDeque


def _run(capacity, ops):
    dq = CircularDeque(capacity)
    return [getattr(dq, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "capacity, ops, expected",
    [
        (
            3,
            [
                ("insert_rear", 1),
                ("insert_rear", 2),
                ("insert_front", 3),
                ("insert_front", 4),
                ("get_rear",),
                ("is_full",),
                ("delete_rear",),
                ("insert_front", 4),
                ("get_front",),
                ("size",),
            ],
            [True, True, True, False, 2, True, 2, True, 4, 3],
        ),
        (
            2,
            [
                ("is_empty",),
                ("get_front",),
                ("get_rear",),
                ("delete_front",),
                ("delete_rear",),
                ("size",),
                ("is_full",),
            ],
            [True, None, None, None, None, 0, False],
        ),
        (  # rear wraps around the end of the array
            3,
            [
                ("insert_rear", 1),
                ("insert_rear", 2),
                ("insert_rear", 3),
                ("delete_front",),
                ("delete_front",),
                ("insert_rear", 4),
                ("insert_rear", 5),
                ("insert_rear", 6),
                ("get_front",),
                ("get_rear",),
                ("delete_front",),
                ("delete_front",),
                ("delete_front",),
                ("delete_front",),
                ("is_empty",),
            ],
            [True, True, True, 1, 2, True, True, False, 3, 5, 3, 4, 5, None, True],
        ),
        (  # front wraps below index 0
            4,
            [
                ("insert_front", 1),
                ("insert_front", 2),
                ("insert_front", 3),
                ("get_rear",),
                ("delete_rear",),
                ("insert_rear", 9),
                ("insert_front", 7),
                ("is_full",),
                ("delete_rear",),
                ("delete_rear",),
                ("delete_rear",),
                ("get_front",),
                ("get_rear",),
                ("delete_front",),
                ("is_empty",),
            ],
            [True, True, True, 1, 1, True, True, True, 9, 2, 3, 7, 7, 7, True],
        ),
        (
            1,
            [
                ("insert_front", 5),
                ("insert_rear", 6),
                ("get_front",),
                ("get_rear",),
                ("delete_rear",),
                ("insert_rear", 6),
                ("delete_front",),
                ("size",),
            ],
            [True, False, 5, 5, 5, True, 6, 0],
        ),
    ],
)
def test_circular_deque(capacity, ops, expected):
    assert _run(capacity, ops) == expected


@pytest.mark.parametrize("seed, capacity", [(0, 1), (1, 3), (2, 5), (3, 8)])
def test_circular_deque_matches_model(seed, capacity):
    rng = random.Random(seed)
    dq, model = CircularDeque(capacity), deque()
    for step in range(400):
        op = rng.choice(
            [
                "insert_front",
                "insert_rear",
                "delete_front",
                "delete_rear",
                "get_front",
                "get_rear",
            ]
        )
        if op.startswith("insert"):
            ok = len(model) < capacity
            if ok:
                (model.appendleft if op == "insert_front" else model.append)(step)
            assert getattr(dq, op)(step) is ok
        elif op.startswith("delete"):
            want = (
                (model.popleft() if op == "delete_front" else model.pop())
                if model
                else None
            )
            assert getattr(dq, op)() == want
        else:
            want = (model[0] if op == "get_front" else model[-1]) if model else None
            assert getattr(dq, op)() == want
        assert dq.size() == len(model)
        assert dq.is_empty() == (not model)
        assert dq.is_full() == (len(model) == capacity)
