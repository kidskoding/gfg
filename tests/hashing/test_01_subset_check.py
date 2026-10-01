import pytest
from helpers import load

is_subset = load("hashing.01_subset_check").is_subset


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7], True),
        ([1, 2, 3, 4, 4, 5, 6], [1, 2, 4], True),
        ([10, 5, 2, 23, 19], [19, 5, 3], False),
        ([1, 2, 3], [1, 1], False),  # b needs two 1s, a has one
        ([1, 2, 3], [], True),
        ([], [1], False),
        ([-1, -1, 0], [-1, -1], True),
        ([5], [5], True),
    ],
)
def test_is_subset(a, b, expected):
    assert is_subset(a, b) is expected
