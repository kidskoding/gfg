import pytest
from helpers import load

can_permute = load("09_sorting.30_pair_sums_at_least_k").can_permute


@pytest.mark.parametrize(
    "a, b, k, expected",
    [
        ([2, 1, 3], [7, 8, 9], 10, True),
        ([1, 2, 2, 1], [3, 3, 3, 4], 5, False),
        ([1, 9], [1, 9], 10, True),
        ([-1, 0], [11, 10], 10, True),
        ([5], [5], 10, True),
        ([5], [4], 10, False),
        ([], [], 5, True),
    ],
)
def test_can_permute(a, b, k, expected):
    assert can_permute(a, b, k) is expected
