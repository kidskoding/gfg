import pytest
from helpers import load

set_kth_bit = load("19_bit_manipulation.04_set_kth_bit").set_kth_bit


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (10, 2, 14),
        (15, 3, 15),  # already set
        (8, 3, 8),
        (0, 0, 1),
        (0, 5, 32),
        (1, 31, 2**31 + 1),
    ],
)
def test_set_kth_bit(n, k, expected):
    assert set_kth_bit(n, k) == expected
