import pytest
from helpers import load

add_overflows = load("bit_manipulation.10_check_integer_overflow").add_overflows


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2**31 - 1, 1, True),
        (-(2**31), -1, True),
        (2**30, 2**30, True),
        (-(2**30), -(2**30) - 1, True),
        (2**30, 2**30 - 1, False),  # exactly INT_MAX
        (-(2**30), -(2**30), False),  # exactly INT_MIN
        (-(2**31), 2**31 - 1, False),
        (5, -7, False),
    ],
)
def test_add_overflows(a, b, expected):
    assert add_overflows(a, b) is expected
