import pytest
from helpers import load

opposite_signs = load("19_bit_manipulation.13_opposite_signs").opposite_signs


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (100, -100, True),
        (-1, 0, True),
        (-(2**31), 2**31 - 1, True),
        (100, 501, False),
        (-10, -10, False),
        (0, 5, False),
        (0, 0, False),
    ],
)
def test_opposite_signs(a, b, expected):
    assert opposite_signs(a, b) is expected
