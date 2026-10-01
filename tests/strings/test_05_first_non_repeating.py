import pytest
from helpers import load

first_non_repeating = load("strings.05_first_non_repeating").first_non_repeating


@pytest.mark.parametrize(
    "s, expected",
    [
        ("geeksforgeeks", "f"),
        ("racecar", "e"),
        ("abcabd", "c"),
        ("zz yy", " "),  # any character counts, including space
        ("aabbcc", None),
        ("a", "a"),
        ("", None),
    ],
)
def test_first_non_repeating(s, expected):
    assert first_non_repeating(s) == expected
