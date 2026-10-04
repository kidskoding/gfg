import pytest
from helpers import load

add_bit_strings = load("19_bit_manipulation.09_add_bit_strings").add_bit_strings


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("1101", "100", "10001"),
        ("1010", "1011", "10101"),
        ("1111", "1", "10000"),
        ("1", "1", "10"),
        ("00011", "01", "100"),  # leading zeros dropped
        ("000", "0000", "0"),
        ("0", "0", "0"),
    ],
)
def test_add_bit_strings(a, b, expected):
    assert add_bit_strings(a, b) == expected
