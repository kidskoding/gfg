import pytest
from helpers import load

intersection_distinct = load(
    "two_pointers.13_intersection_distinct"
).intersection_distinct


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [3, 4, 5]),
        ([5, 6, 2, 1, 4], [7, 9, 4, 2], [2, 4]),
        ([-1, 0, 1], [1, -1], [-1, 1]),
        ([1, 3], [2, 4], []),
        ([7], [7], [7]),
        ([], [1], []),
    ],
)
def test_intersection_distinct(a, b, expected):
    assert intersection_distinct(a, b) == expected
