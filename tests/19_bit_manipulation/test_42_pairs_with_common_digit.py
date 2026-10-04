import pytest
from helpers import load

count_common_digit_pairs = load(
    "19_bit_manipulation.42_pairs_with_common_digit"
).count_common_digit_pairs


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 12, 24], 2),
        ([9999, 7676, 66, 2], 1),
        ([0, 10, 100], 3),  # all share 0
        ([1, 1, 1], 3),
        ([12, 34, 56], 0),
        ([5], 0),
        ([], 0),
    ],
)
def test_count_common_digit_pairs(arr, expected):
    assert count_common_digit_pairs(arr) == expected
