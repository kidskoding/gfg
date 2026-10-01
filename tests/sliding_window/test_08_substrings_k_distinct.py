import pytest
from helpers import load

count_k_distinct = load("sliding_window.08_substrings_k_distinct").count_k_distinct


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abc", 2, 2),
        ("aba", 2, 3),
        ("abaaca", 1, 7),
        ("aa", 1, 3),
        ("abcabc", 3, 10),
        ("abc", 4, 0),  # k exceeds distinct chars
        ("", 1, 0),
    ],
)
def test_count_k_distinct(s, k, expected):
    assert count_k_distinct(s, k) == expected
