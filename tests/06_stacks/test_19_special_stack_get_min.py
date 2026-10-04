import pytest
from helpers import load

SpecialStack = load("06_stacks.19_special_stack_get_min").SpecialStack


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
    ],
)
def test_special_stack(args, ops, expected):
    assert _run(SpecialStack(*args), ops) == expected
