import pytest
from helpers import load

smallest_difference_triplet = load(
    "10_searching.32_smallest_difference_triplet"
).smallest_difference_triplet


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        ([5, 2, 8], [10, 7, 12], [9, 14, 6], [7, 6, 5]),
        ([15, 12, 18, 9], [10, 17, 13, 8], [14, 16, 11, 5], [11, 10, 9]),
        (
            [1, 4],
            [2, 5],
            [3, 6],
            [3, 2, 1],
        ),  # (1,2,3) and (4,5,6) tie on range: smaller sum
        ([10], [1, 20], [11, 30], [11, 10, 1]),
        ([1, 100], [2, 200], [3, 300], [3, 2, 1]),
        ([1], [1], [1], [1, 1, 1]),
    ],
)
def test_smallest_difference_triplet(a, b, c, expected):
    assert list(smallest_difference_triplet(a, b, c)) == expected
