import pytest
from helpers import load

sorted_union = load("04_two_pointers.18_union_sorted_with_dups").sorted_union


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([2, 2, 3, 4, 5], [1, 1, 2, 3, 4], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [1, 2]),
        ([-2, -2, 0], [-1, 0], [-2, -1, 0]),
        ([], [3, 3], [3]),
        ([], [], []),
    ],
)
def test_sorted_union(a, b, expected):
    assert sorted_union(a, b) == expected
