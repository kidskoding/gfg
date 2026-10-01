import pytest
from helpers import load

KStacks = load("stacks.31_k_stacks_in_array").KStacks


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            (3, 10),
            [
                ("push", 15, 2),
                ("push", 45, 2),
                ("push", 17, 1),
                ("push", 49, 1),
                ("push", 39, 1),
                ("push", 11, 0),
                ("push", 9, 0),
                ("push", 7, 0),
                ("pop", 2),
                ("pop", 1),
                ("pop", 0),
            ],
            [True] * 8 + [45, 39, 7],
        ),
        (
            (2, 3),
            [
                ("push", 1, 0),
                ("push", 2, 1),
                ("push", 3, 1),
                ("push", 4, 0),
                ("pop", 1),
                ("push", 5, 0),
                ("pop", 0),
                ("pop", 0),
                ("pop", 0),
                ("is_empty", 0),
                ("is_empty", 1),
                ("pop", 1),
                ("is_empty", 1),
            ],
            [True, True, True, False, 3, True, 5, 1, None, True, False, 2, True],
        ),
        (
            (1, 2),
            [
                ("push", 1, 0),
                ("push", 2, 0),
                ("push", 3, 0),
                ("pop", 0),
                ("push", 4, 0),
                ("pop", 0),
                ("pop", 0),
                ("pop", 0),
            ],
            [True, True, False, 2, True, 4, 1, None],
        ),
        (
            (3, 3),
            [
                ("push", 1, 2),
                ("push", 2, 2),
                ("push", 3, 2),
                ("push", 4, 0),
                ("is_empty", 0),
                ("pop", 2),
                ("push", 4, 0),
                ("pop", 0),
                ("pop", 2),
            ],
            [True, True, True, False, True, 3, True, 4, 2],
        ),
    ],
)
def test_k_stacks(args, ops, expected):
    assert _run(KStacks(*args), ops) == expected
