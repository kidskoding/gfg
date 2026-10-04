import pytest
from helpers import load

kth_in_multiplication_table = load(
    "10_searching.42_kth_in_multiplication_table"
).kth_in_multiplication_table


@pytest.mark.parametrize(
    "m, n, k, expected",
    [
        (3, 3, 5, 3),
        (2, 3, 6, 6),
        (4, 2, 5, 4),
        (3, 3, 9, 9),  # largest entry
        (3, 3, 1, 1),
        (1, 5, 3, 3),  # single row
        (1, 1, 1, 1),
    ],
)
def test_kth_in_multiplication_table(m, n, k, expected):
    assert kth_in_multiplication_table(m, n, k) == expected
