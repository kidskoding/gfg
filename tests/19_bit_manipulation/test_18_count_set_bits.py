import pytest
from helpers import load

count_set_bits = load("19_bit_manipulation.18_count_set_bits").count_set_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        (6, 2),
        (13, 3),
        (255, 8),
        (1023, 10),
        (2**31 - 1, 31),
        (2**40, 1),
        (1, 1),
        (0, 0),
    ],
)
def test_count_set_bits(n, expected):
    assert count_set_bits(n) == expected
