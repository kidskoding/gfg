import pytest
from helpers import load
from helpers.linked_lists import build_list

multiply_numbers = load("linked_lists.26_multiply_two_numbers").multiply_numbers
MOD = 1_000_000_007


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([3, 2], [2], 64),
        ([1, 0, 0], [1, 0], 1000),
        ([9, 4, 6], [8, 4], 79464),
        ([0, 0, 1, 2], [0, 3], 36),  # leading zeros
        ([0], [1, 2, 3], 0),
        ([7], [8], 56),
        ([9] * 12, [9] * 12, 999_999_999_999**2 % MOD),  # needs the modulo
        ([1, 0, 0, 0, 0, 0, 0, 0, 0, 7], [1], 0),  # 1_000_000_007 % MOD
    ],
)
def test_multiply_numbers(a, b, expected):
    assert multiply_numbers(build_list(a), build_list(b)) == expected
