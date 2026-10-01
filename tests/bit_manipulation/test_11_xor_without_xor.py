import pytest
from helpers import load

xor_without_xor = load("bit_manipulation.11_xor_without_xor").xor_without_xor


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),
        (3, 5, 6),
        (1000, 1, 1001),
        (123456, 654321, 530865),
        (7, 7, 0),
        (0, 9, 9),
        (0, 0, 0),
    ],
)
def test_xor_without_xor(x, y, expected):
    assert xor_without_xor(x, y) == expected
