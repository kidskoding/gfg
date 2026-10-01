import pytest
from helpers import load

count_equal_012 = load("strings.19_equal_012_substrings").count_equal_012


@pytest.mark.parametrize(
    "s, expected",
    [
        ("0102010", 2),
        ("102100211", 5),
        ("012012", 5),
        ("012", 1),
        ("000", 0),
        ("0", 0),
        ("", 0),
    ],
)
def test_count_equal_012(s, expected):
    assert count_equal_012(s) == expected
