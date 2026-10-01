import pytest
from helpers import load

karatsuba = load("bit_manipulation.35_karatsuba_multiplication").karatsuba


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("1100", "1010", 120),
        ("110", "1010", 60),
        ("11", "1", 3),
        ("11111111", "11111111", 65025),
        ("1" * 20, "1" * 20, 1099509530625),
        ("1", "1", 1),
        ("0", "1111", 0),
        ("0011", "010", 6),  # leading zeros
    ],
)
def test_karatsuba(a, b, expected):
    assert karatsuba(a, b) == expected
