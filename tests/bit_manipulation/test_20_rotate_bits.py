import pytest
from helpers import load

rotate_bits = load("bit_manipulation.20_rotate_bits").rotate_bits


@pytest.mark.parametrize(
    "n, d, width, expected",
    [
        (229, 3, 16, (1832, 40988)),
        (28, 2, 16, (112, 7)),
        (229, 19, 16, (1832, 40988)),  # d wraps around the width
        (1, 1, 16, (2, 32768)),
        (32768, 1, 16, (1, 16384)),
        (65535, 7, 16, (65535, 65535)),
        (0, 5, 16, (0, 0)),
        (1, 1, 32, (2, 2**31)),
        (16, 2, 32, (64, 4)),
    ],
)
def test_rotate_bits(n, d, width, expected):
    assert rotate_bits(n, d, width) == expected


def test_rotate_bits_default_width_is_16():
    assert rotate_bits(1, 1) == (2, 32768)
