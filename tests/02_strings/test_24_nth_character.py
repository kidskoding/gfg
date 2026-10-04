import pytest
from helpers import load

nth_char = load("02_strings.24_nth_character").nth_char


@pytest.mark.parametrize(
    "m, n, k, expected",
    [
        (5, 2, 5, "0"),  # 101 -> 100110 -> 100101101001
        (5, 2, 1, "1"),
        (5, 2, 12, "1"),
        (5, 0, 2, "0"),  # zero iterations: binary itself
        (1, 3, 4, "1"),  # 1 -> 10 -> 1001 -> 10010110
        (1, 3, 8, "0"),
        (0, 2, 3, "1"),  # 0 -> 01 -> 0110
    ],
)
def test_nth_char(m, n, k, expected):
    assert nth_char(m, n, k) == expected
