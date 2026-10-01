import pytest
from helpers import load

MinStack = load("stacks.28_min_stack_constant_space").MinStack


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            (),
            [
                ("push", 18),
                ("push", 19),
                ("push", 29),
                ("push", 15),
                ("push", 16),
                ("get_min",),
                ("pop",),
                ("pop",),
                ("get_min",),
                ("peek",),
            ],
            [None, None, None, None, None, 15, 16, 15, 18, 29],
        ),
        (
            (),
            [
                ("push", 2),
                ("push", 2),
                ("push", 3),
                ("get_min",),
                ("pop",),
                ("pop",),
                ("get_min",),
                ("pop",),
                ("get_min",),
                ("pop",),
                ("peek",),
            ],
            [None, None, None, 2, 3, 2, 2, 2, None, None, None],
        ),
        (
            (),
            [
                ("push", 5),
                ("push", -1),
                ("push", 3),
                ("get_min",),
                ("pop",),
                ("get_min",),
                ("pop",),
                ("get_min",),
            ],
            [None, None, None, -1, 3, -1, -1, 5],
        ),
        (
            (),
            [
                ("push", 3),
                ("push", 2),
                ("push", 1),
                ("get_min",),
                ("pop",),
                ("get_min",),
                ("pop",),
                ("get_min",),
                ("peek",),
            ],
            [None, None, None, 1, 1, 2, 2, 3, 3],
        ),
        ((), [("get_min",), ("pop",), ("peek",)], [None, None, None]),
        (
            (),
            [
                ("push", 10**12),
                ("push", -(10**12)),
                ("peek",),
                ("get_min",),
                ("pop",),
                ("peek",),
                ("get_min",),
            ],
            [None, None, -(10**12), -(10**12), -(10**12), 10**12, 10**12],
        ),
        (
            (),
            [
                ("push", 0),
                ("push", -4),
                ("push", 7),
                ("push", -4),
                ("pop",),
                ("get_min",),
                ("pop",),
                ("pop",),
                ("get_min",),
            ],
            [None, None, None, None, -4, -4, 7, -4, 0],
        ),
    ],
)
def test_min_stack(args, ops, expected):
    assert _run(MinStack(*args), ops) == expected
