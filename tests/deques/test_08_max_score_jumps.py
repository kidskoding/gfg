import pytest
from helpers import load

max_score = load("deques.08_max_score_jumps").max_score


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([100, -30, -50, -15, -20, -30], 3, 55),
        ([10, -5, -2, 4, 0, 3], 3, 17),
        ([1, -1, -2, -3, 4], 1, -1),  # k = 1 visits everything
        ([1, -10, -10, 2], 2, -7),
        ([3, -1, -1, -1, 5], 10, 8),  # jump straight to the end
        ([-1, -2, -3], 2, -4),
        ([2, 2, 2, 2], 2, 8),  # positives: take every step
        ([5], 2, 5),
    ],
)
def test_max_score(arr, k, expected):
    assert max_score(arr, k) == expected
