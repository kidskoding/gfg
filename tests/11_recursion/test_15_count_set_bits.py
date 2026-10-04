import pytest
from helpers import load

count_set_bits = load("11_recursion.15_count_set_bits").count_set_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        (13, 3),
        (6, 2),
        (8, 1),
        (0, 0),
        (1, 1),
        (255, 8),
        (1023, 10),
        (2**40, 1),
    ],
)
def test_count_set_bits(n, expected):
    assert count_set_bits(n) == expected
