import pytest
from helpers import load

subsets = load("11_recursion.28_subsets").subsets


def _norm(sets):
    return sorted(tuple(s) for s in sets)


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([5], [[], [5]]),
        ([], [[]]),
        ([3, 1], [[], [3], [1], [3, 1]]),  # each subset keeps input order
        (
            [2, 2],
            [[], [2], [2], [2, 2]],
        ),  # by index: duplicate values give repeat subsets
        ([-1, 0], [[], [-1], [0], [-1, 0]]),
    ],
)
def test_subsets(arr, expected):
    assert _norm(subsets(arr)) == _norm(expected)


def test_subsets_count():
    assert len(subsets(list(range(10)))) == 1024
