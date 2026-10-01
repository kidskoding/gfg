import pytest
from helpers import load

gray_codes = load("bit_manipulation.26_gray_codes").gray_codes


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["0", "1"]),
        (2, ["00", "01", "11", "10"]),
        (3, ["000", "001", "011", "010", "110", "111", "101", "100"]),
    ],
)
def test_gray_codes(n, expected):
    assert gray_codes(n) == expected


@pytest.mark.parametrize("n", [4, 5, 8])
def test_gray_codes_properties(n):
    codes = gray_codes(n)
    assert len(codes) == 2**n
    assert len(set(codes)) == 2**n
    assert all(len(c) == n and set(c) <= {"0", "1"} for c in codes)
    for a, b in zip(codes, codes[1:] + codes[:1]):
        assert sum(x != y for x, y in zip(a, b)) == 1
