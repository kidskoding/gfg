import pytest
from helpers import load

count_digit_sum_diff = load(
    "searching.43_count_digit_sum_difference"
).count_digit_sum_diff


@pytest.mark.parametrize(
    "n, d, expected",
    [
        (13, 2, 4),
        (14, 3, 5),
        (100, 9, 91),
        (100, 10, 81),
        (100, 0, 100),  # every number qualifies
        (9, 0, 9),
        (1, 1, 0),
        (1000, 1000, 0),
    ],
)
def test_count_digit_sum_diff(n, d, expected):
    assert count_digit_sum_diff(n, d) == expected
