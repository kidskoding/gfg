import pytest
from helpers import load

word_break = load("11_recursion.39_word_break").word_break

GFG_DICT = [
    "i",
    "like",
    "sam",
    "sung",
    "samsung",
    "mobile",
    "ice",
    "cream",
    "icecream",
    "man",
    "go",
    "mango",
]


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("ilike", GFG_DICT, True),
        ("ilikesamsung", GFG_DICT, True),
        ("iiiiiiii", GFG_DICT, True),
        ("ilikelikeimangoiii", GFG_DICT, True),
        ("samsungandmango", GFG_DICT, False),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("applepenapple", ["apple", "pen"], True),  # words can be reused
        ("", ["a"], True),
        ("a", [], False),
    ],
)
def test_word_break(s, words, expected):
    assert word_break(s, words) is expected
