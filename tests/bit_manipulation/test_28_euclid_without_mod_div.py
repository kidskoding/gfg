import pytest
from helpers import load

binary_gcd = load("bit_manipulation.28_euclid_without_mod_div").binary_gcd


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (12, 18, 6),
        (48, 180, 12),
        (17, 5, 1),
        (1024, 64, 64),
        (2**40, 6, 2),
        (0, 7, 7),
        (7, 0, 7),
        (0, 0, 0),
    ],
)
def test_binary_gcd(a, b, expected):
    assert binary_gcd(a, b) == expected
