import pytest
from helpers import load

_mod = load("19_bit_manipulation.30_crc_modulo_two_division")
crc_encode = _mod.crc_encode
crc_check = _mod.crc_check


@pytest.mark.parametrize(
    "data, key, expected",
    [
        ("100100", "1101", "100100001"),
        ("11010011101100", "1011", "11010011101100100"),
        ("1101011011", "10011", "11010110111110"),
        ("1", "11", "11"),
        ("0000", "101", "000000"),
    ],
)
def test_crc_encode(data, key, expected):
    assert crc_encode(data, key) == expected


@pytest.mark.parametrize(
    "codeword, key, expected",
    [
        ("100100001", "1101", True),
        ("11010011101100100", "1011", True),
        ("100100011", "1101", False),  # one bit flipped
        ("11010011101100101", "1011", False),
        ("000000", "101", True),
    ],
)
def test_crc_check(codeword, key, expected):
    assert crc_check(codeword, key) is expected


@pytest.mark.parametrize("data", ["1", "1011", "111000111", "100000000001"])
def test_crc_round_trip_and_single_bit_errors(data):
    key = "1011"
    codeword = crc_encode(data, key)
    assert len(codeword) == len(data) + 3
    assert codeword.startswith(data)
    assert crc_check(codeword, key)
    for i in range(len(codeword)):
        flipped = (
            codeword[:i] + ("1" if codeword[i] == "0" else "0") + codeword[i + 1 :]
        )
        assert not crc_check(flipped, key)
