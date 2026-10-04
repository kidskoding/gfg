import pytest
from helpers import load

MiddleStack = load("06_stacks.37_stack_with_middle_ops").MiddleStack


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            (),
            [("push", x) for x in (11, 22, 33, 44, 55, 66, 77)]
            + [
                ("find_middle",),
                ("pop",),
                ("pop",),
                ("find_middle",),
                ("delete_middle",),
                ("find_middle",),
            ],
            [None] * 7 + [44, 77, 66, 33, 33, 22],
        ),
        (
            (),
            [("push", x) for x in range(1, 8)]
            + [
                ("delete_middle",),
                ("find_middle",),
                ("pop",),
                ("find_middle",),
                ("delete_middle",),
                ("find_middle",),
            ],
            [None] * 7 + [4, 3, 7, 3, 3, 2],
        ),
        (
            (),
            [
                ("push", 1),
                ("find_middle",),
                ("push", 2),
                ("find_middle",),
                ("push", 3),
                ("delete_middle",),
                ("find_middle",),
                ("delete_middle",),
                ("find_middle",),
                ("pop",),
                ("find_middle",),
            ],
            [None, 1, None, 1, None, 2, 1, 1, 3, 3, None],
        ),
        ((), [("find_middle",), ("delete_middle",), ("pop",)], [None, None, None]),
    ],
)
def test_middle_stack(args, ops, expected):
    assert _run(MiddleStack(*args), ops) == expected
