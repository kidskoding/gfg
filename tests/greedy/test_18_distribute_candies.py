import pytest
from helpers import load

min_candies = load("greedy.18_distribute_candies").min_candies


@pytest.mark.parametrize(
    "ratings, expected",
    [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),  # equal neighbours need not differ
        ([1, 3, 2, 2, 1], 7),
        ([1, 3, 4, 5, 2], 11),
        ([1, 2, 3, 4], 10),
        ([4, 3, 2, 1], 10),
        ([3, 3, 3], 3),
        ([5], 1),
        ([], 0),
    ],
)
def test_min_candies(ratings, expected):
    assert min_candies(ratings) == expected
