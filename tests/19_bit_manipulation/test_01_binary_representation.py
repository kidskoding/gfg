import pytest
from helpers import load

binary_representation = load(
    "19_bit_manipulation.01_binary_representation"
).binary_representation


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (7, "111"),
        (10, "1010"),
        (2**31 - 1, "1" * 31),
        (2**40, "1" + "0" * 40),
    ],
)
def test_binary_representation(n, expected):
    assert binary_representation(n) == expected
