import pytest
from helpers import load

bitonic_sequence = load("deques.12_bitonic_sequence_in_range").bitonic_sequence


@pytest.mark.parametrize(
    "n, low, high, expected",
    [
        (5, 3, 10, [9, 10, 9, 8, 7]),
        (7, 2, 5, [2, 3, 4, 5, 4, 3, 2]),  # longest possible
        (6, 1, 4, [2, 3, 4, 3, 2, 1]),
        (4, 1, 3, [2, 3, 2, 1]),
        (4, -2, 3, [2, 3, 2, 1]),
        (3, 0, 100, [99, 100, 99]),
        (3, 1, 2, [1, 2, 1]),
        (8, 2, 5, []),  # too long
        (3, 5, 5, []),  # single value cannot rise
    ],
)
def test_bitonic_sequence(n, low, high, expected):
    assert bitonic_sequence(n, low, high) == expected
