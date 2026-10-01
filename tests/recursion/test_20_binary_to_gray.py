import pytest
from helpers import load

binary_to_gray = load("recursion.20_binary_to_gray").binary_to_gray


@pytest.mark.parametrize(
    "binary, expected",
    [
        ("1001", "1101"),
        ("11", "10"),
        ("1010", "1111"),
        ("0", "0"),
        ("1", "1"),
        ("0011", "0010"),  # leading zeros are kept
        ("1111", "1000"),
        ("", ""),
    ],
)
def test_binary_to_gray(binary, expected):
    assert binary_to_gray(binary) == expected
