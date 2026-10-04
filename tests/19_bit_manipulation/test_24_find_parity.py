import pytest
from helpers import load

has_odd_parity = load("19_bit_manipulation.24_find_parity").has_odd_parity


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, True),
        (7, True),
        (13, True),
        (2**31, True),
        (9, False),
        (255, False),
        (2**32 - 1, False),
        (0, False),
    ],
)
def test_has_odd_parity(n, expected):
    assert has_odd_parity(n) is expected
