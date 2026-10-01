import random
from collections import deque

import pytest
from helpers import load

LinkedDeque = load("deques.02_dll_deque").LinkedDeque


def _run(ops):
    dq = LinkedDeque()
    return [getattr(dq, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "ops, expected",
    [
        (
            [
                ("push_back", 1),
                ("push_back", 2),
                ("push_front", 0),
                ("front",),
                ("back",),
                ("size",),
                ("pop_back",),
                ("pop_front",),
                ("pop_front",),
                ("pop_front",),
                ("is_empty",),
            ],
            [None, None, None, 0, 2, 3, 2, 0, 1, None, True],
        ),
        (
            [
                ("front",),
                ("back",),
                ("pop_back",),
                ("pop_front",),
                ("size",),
                ("is_empty",),
            ],
            [None, None, None, None, 0, True],
        ),
        (
            [
                ("push_front", 1),
                ("push_front", 2),
                ("pop_back",),
                ("pop_back",),
                ("pop_back",),
                ("push_back", 3),
                ("front",),
                ("back",),
                ("is_empty",),
            ],
            [None, None, 1, 2, None, None, 3, 3, False],
        ),
        (
            [
                ("push_back", 1),
                ("push_back", 2),
                ("clear",),
                ("size",),
                ("front",),
                ("push_front", 5),
                ("back",),
                ("size",),
            ],
            [None, None, None, 0, None, None, 5, 1],
        ),
        (  # duplicates
            [("push_back", 7), ("push_front", 7), ("pop_front",), ("size",), ("back",)],
            [None, None, 7, 1, 7],
        ),
    ],
)
def test_linked_deque(ops, expected):
    assert _run(ops) == expected


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_linked_deque_matches_model(seed):
    rng = random.Random(seed)
    dq, model = LinkedDeque(), deque()
    for step in range(400):
        op = rng.choice(
            [
                "push_front",
                "push_back",
                "pop_front",
                "pop_back",
                "front",
                "back",
                "clear",
            ]
        )
        if op == "push_front":
            dq.push_front(step)
            model.appendleft(step)
        elif op == "push_back":
            dq.push_back(step)
            model.append(step)
        elif op == "pop_front":
            assert dq.pop_front() == (model.popleft() if model else None)
        elif op == "pop_back":
            assert dq.pop_back() == (model.pop() if model else None)
        elif op == "front":
            assert dq.front() == (model[0] if model else None)
        elif op == "back":
            assert dq.back() == (model[-1] if model else None)
        elif rng.random() < 0.2:
            dq.clear()
            model.clear()
        assert dq.size() == len(model)
        assert dq.is_empty() == (not model)
