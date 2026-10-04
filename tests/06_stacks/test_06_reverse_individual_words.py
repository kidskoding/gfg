import pytest
from helpers import load

reverse_words = load("06_stacks.06_reverse_individual_words").reverse_words


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", "olleH dlroW"),
        ("i like this program very much", "i ekil siht margorp yrev hcum"),
        ("Geeks for Geeks", "skeeG rof skeeG"),
        ("  ab  cd ", "  ba  dc "),
        ("abc", "cba"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_reverse_words(s, expected):
    assert reverse_words(s) == expected
