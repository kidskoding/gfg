import pytest
from helpers import load

longest_ones_one_flip = load(
    "bit_manipulation.37_longest_ones_one_flip"
).longest_ones_one_flip


@pytest.mark.parametrize(
    "n, expected",
    [
        (1775, 8),  # 11011101111
        (12, 3),
        (71, 4),  # 1000111
        (15, 5),  # flip the zero above the top bit
        (2**31, 2),
        (2**32 - 1, 32),  # nothing to flip
        (0, 1),
    ],
)
def test_longest_ones_one_flip(n, expected):
    assert longest_ones_one_flip(n) == expected
