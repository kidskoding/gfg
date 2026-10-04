import pytest
from helpers import load

parity_lookup = load("19_bit_manipulation.40_parity_lookup_table").parity_lookup


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (13, 1),
        (0x80000000, 1),
        (0x12345678, 1),  # 13 set bits
        (9, 0),
        (0xFF00FF00, 0),
        (2**32 - 1, 0),
        (0, 0),
    ],
)
def test_parity_lookup(n, expected):
    assert parity_lookup(n) == expected
