import pytest
from helpers import load

TwoStacks = load("06_stacks.04_two_stacks_in_array").TwoStacks


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            (5,),
            [("push1", 2), ("push1", 3), ("push2", 4), ("pop1",), ("pop2",), ("pop2",)],
            [True, True, True, 3, 4, None],
        ),
        (
            (3,),
            [
                ("push1", 1),
                ("push2", 2),
                ("push2", 3),
                ("push1", 4),
                ("push2", 5),
                ("pop2",),
                ("push1", 6),
                ("pop1",),
                ("pop1",),
                ("pop1",),
            ],
            [True, True, True, False, False, 3, True, 6, 1, None],
        ),
        (
            (1,),
            [("pop1",), ("push2", 7), ("push1", 8), ("pop2",), ("push1", 9), ("pop1",)],
            [None, True, False, 7, True, 9],
        ),
        (
            (4,),
            [
                ("push1", 1),
                ("push1", 2),
                ("push1", 3),
                ("push1", 4),
                ("push2", 5),
                ("pop2",),
                ("pop1",),
            ],
            [True, True, True, True, False, None, 4],
        ),
        (
            (2,),
            [("push2", 1), ("push2", 2), ("push1", 3), ("pop2",), ("pop2",), ("pop2",)],
            [True, True, False, 2, 1, None],
        ),
    ],
)
def test_two_stacks(args, ops, expected):
    assert _run(TwoStacks(*args), ops) == expected
