import random

import pytest
from helpers import load

RandomizedCollection = load("06_stacks.29_randomized_collection").RandomizedCollection


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            (),
            [
                ("insert", 1),
                ("insert", 1),
                ("insert", 2),
                ("remove", 1),
                ("remove", 1),
                ("remove", 1),
                ("get_random",),
            ],
            [True, False, True, True, True, False, 2],
        ),
        (
            (),
            [("remove", 5), ("get_random",), ("insert", 5), ("get_random",)],
            [False, None, True, 5],
        ),
        (
            (),
            [
                ("insert", 4),
                ("insert", 4),
                ("remove", 4),
                ("get_random",),
                ("remove", 4),
                ("get_random",),
            ],
            [True, False, True, 4, True, None],
        ),
    ],
)
def test_randomized_collection(args, ops, expected):
    assert _run(RandomizedCollection(*args), ops) == expected


def test_get_random_only_returns_present_values():
    c = RandomizedCollection()
    for x in (1, 2, 3, 2):
        c.insert(x)
    c.remove(2)
    c.remove(3)
    assert {c.get_random() for _ in range(200)} <= {1, 2}
    c.remove(2)
    assert {c.get_random() for _ in range(50)} == {1}


def test_get_random_weighted_by_copies():
    random.seed(0)
    c = RandomizedCollection()
    for x in (1, 1, 1, 2):
        c.insert(x)
    draws = [c.get_random() for _ in range(4000)]
    assert set(draws) == {1, 2}
    assert 0.68 < draws.count(1) / len(draws) < 0.82
