import pytest
from helpers import load

min_sum_from_digits = load("14_heaps.05_min_sum_from_digits").min_sum_from_digits


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([6, 8, 4, 5, 2, 3], 604),  # 246 + 358
        ([5, 3, 0, 7, 4], 82),  # 047 + 35
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 16047),  # 13579 + 2468
        ([9, 4], 13),
        ([0, 0, 1], 1),
        ([0, 0], 0),
        ([5], 5),
    ],
)
def test_min_sum_from_digits(digits, expected):
    assert min_sum_from_digits(digits) == expected
