import pytest
from helpers import load
from helpers.trees import build

is_subtree = load("trees.13_check_if_subtree").is_subtree


@pytest.mark.parametrize(
    "t, s, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [2, 4, 5], True),
        ([1, 2, 3, 4, 5, 6, 7], [2, 4], False),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], True),
        ([1, 2, 3, 4, 5, 6, 7], [7], True),
        ([1, 2, 3, 4, 5, 6, 7], [8], False),
        ([1, 2, 3], [1, 2, 3, 4], False),
        ([1, 2, 3], [], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ],
)
def test_is_subtree(t, s, expected):
    assert is_subtree(build(t), build(s)) is expected
