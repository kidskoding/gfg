import pytest
from helpers import load

is_kth_bit_set = load("bit_manipulation.03_is_kth_bit_set").is_kth_bit_set


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (5, 0, True),
        (5, 1, False),
        (5, 2, True),
        (4, 2, True),
        (500, 3, False),
        (10, 10, False),  # k beyond the highest bit
        (0, 0, False),
        (1 << 40, 40, True),
    ],
)
def test_is_kth_bit_set(n, k, expected):
    assert is_kth_bit_set(n, k) is expected
