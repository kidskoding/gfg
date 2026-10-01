import pytest
from helpers import load

reverse_words = load("strings.03_reverse_words").reverse_words


@pytest.mark.parametrize(
    "s, expected",
    [
        ("i like this program very much", "much very program this like i"),
        ("geeks for geeks", "geeks for geeks"),
        ("  hello   world  ", "world hello"),  # collapse and trim spaces
        ("a b", "b a"),
        ("single", "single"),
        ("   ", ""),
        ("", ""),
    ],
)
def test_reverse_words(s, expected):
    assert reverse_words(s) == expected
