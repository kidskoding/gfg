import pytest
from helpers import load

_mod = load("bit_manipulation.33_gray_binary_conversion")
binary_to_gray = _mod.binary_to_gray
gray_to_binary = _mod.gray_to_binary


@pytest.mark.parametrize(
    "binary, gray",
    [
        ("01001", "01101"),
        ("1111", "1000"),
        ("100", "110"),
        ("0000", "0000"),
        ("0", "0"),
        ("1", "1"),
    ],
)
def test_binary_to_gray(binary, gray):
    assert binary_to_gray(binary) == gray


@pytest.mark.parametrize(
    "binary, gray",
    [
        ("01001", "01101"),
        ("1111", "1000"),
        ("100", "110"),
        ("0000", "0000"),
        ("0", "0"),
        ("1", "1"),
    ],
)
def test_gray_to_binary(binary, gray):
    assert gray_to_binary(gray) == binary


def test_round_trip_all_5_bit_strings():
    for i in range(32):
        b = format(i, "05b")
        assert binary_to_gray(b) == format(i ^ (i >> 1), "05b")
        assert gray_to_binary(binary_to_gray(b)) == b
