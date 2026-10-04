import pytest
from helpers import load

is_bleak = load("19_bit_manipulation.32_check_bleak").is_bleak


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, False),  # 2 + 1
        (4, True),
        (1, True),
        (6, True),
        (2, False),  # 1 + 1
        (5, False),  # 4 + 1
        (7, False),  # 5 + 2
        (0, False),  # 0 + 0
    ],
)
def test_is_bleak(n, expected):
    assert is_bleak(n) is expected
