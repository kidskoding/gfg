import pytest
from helpers import load

closest_same_bits = load("19_bit_manipulation.38_closest_same_set_bits").closest_same_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, (3, 6)),
        (11, (7, 13)),
        (6, (5, 9)),
        (10, (9, 12)),
        (8, (4, 16)),
        (3, (-1, 5)),  # 11 is the smallest with two bits
        (1, (-1, 2)),
    ],
)
def test_closest_same_bits(n, expected):
    assert closest_same_bits(n) == expected
