import pytest
from helpers import load

word_break = load("18_dynamic_programming.16_word_break").word_break


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("ilike", ["i", "like", "sam", "sung", "samsung"], True),
        ("ilikesamsung", ["i", "like", "sam", "sung", "samsung"], True),
        ("ilikemangoes", ["i", "like", "man", "go"], False),
        ("applepenapple", ["apple", "pen"], True),  # reuse
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("aaaaaaab", ["a", "aa", "aaa"], False),
        ("abc", [], False),
        ("", ["a"], True),
    ],
)
def test_word_break(s, words, expected):
    assert word_break(s, words) == expected
