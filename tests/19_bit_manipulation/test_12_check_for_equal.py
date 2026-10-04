import pytest
from helpers import load

are_equal = load("19_bit_manipulation.12_check_for_equal").are_equal


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 10, True),
        (10, 20, False),
        (0, 0, True),
        (-5, -5, True),
        (-5, 5, False),
        (1, 0, False),
    ],
)
def test_are_equal(a, b, expected):
    assert are_equal(a, b) is expected
