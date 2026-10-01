import pytest
from helpers import load

float_to_binary = load("bit_manipulation.43_float_to_binary").float_to_binary


@pytest.mark.parametrize(
    "x, places, expected",
    [
        (1.234, 4, "1.0011"),
        (10.25, 2, "1010.01"),
        (3.75, 4, "11.1100"),  # pads with zeros
        (2.625, 5, "10.10100"),
        (0.1, 8, "0.00011001"),  # truncated, not rounded
        (0.5, 3, "0.100"),
        (0.0, 2, "0.00"),
    ],
)
def test_float_to_binary(x, places, expected):
    assert float_to_binary(x, places) == expected
