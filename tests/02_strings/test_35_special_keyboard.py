import pytest
from helpers import load

max_a = load("02_strings.35_special_keyboard").max_a


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (3, 3),
        (6, 6),
        (7, 9),
        (8, 12),
        (11, 27),
        (15, 81),
    ],
)
def test_max_a(n, expected):
    assert max_a(n) == expected
