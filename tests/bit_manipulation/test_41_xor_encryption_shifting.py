import pytest
from helpers import load

decrypt_shift_xor = load(
    "bit_manipulation.41_xor_encryption_shifting"
).decrypt_shift_xor


def _encrypt(plain, k):
    cols = [0] * (len(plain) + k - 1)
    for shift in range(k):
        for i, ch in enumerate(plain):
            cols[i + shift] ^= int(ch)
    return "".join(map(str, cols))


@pytest.mark.parametrize(
    "cipher, k, expected",
    [
        ("1110100110", 4, "1001010"),
        ("1110001", 2, "101111"),
        ("1011", 1, "1011"),  # k = 1: no mixing
        ("111", 3, "1"),
        ("1", 1, "1"),
        ("0000", 2, "000"),
    ],
)
def test_decrypt_shift_xor(cipher, k, expected):
    assert decrypt_shift_xor(cipher, k) == expected


@pytest.mark.parametrize(
    "plain, k",
    [("110100111010", 5), ("0110", 4), ("1", 6), ("101", 3), ("1" * 10, 7)],
)
def test_decrypt_shift_xor_round_trip(plain, k):
    assert decrypt_shift_xor(_encrypt(plain, k), k) == plain
