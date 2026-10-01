import pytest
from helpers import load

only_set_bit_position = load(
    "bit_manipulation.08_only_set_bit_position"
).only_set_bit_position


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 2),
        (1, 1),
        (128, 8),
        (2**31, 32),
        (5, -1),
        (3, -1),
        (0, -1),
    ],
)
def test_only_set_bit_position(n, expected):
    assert only_set_bit_position(n) == expected
