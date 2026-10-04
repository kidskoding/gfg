import pytest
from helpers import load

next_higher_same_bits = load(
    "19_bit_manipulation.34_next_higher_same_set_bits"
).next_higher_same_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 6),
        (6, 9),
        (156, 163),
        (12, 17),
        (7, 11),
        (3, 5),
        (8, 16),
        (1, 2),
    ],
)
def test_next_higher_same_bits(n, expected):
    assert next_higher_same_bits(n) == expected
