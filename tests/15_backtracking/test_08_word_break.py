import pytest
from helpers import load

word_break = load("15_backtracking.08_word_break").word_break

GFG_DICT = [
    "i",
    "like",
    "sam",
    "sung",
    "samsung",
    "mobile",
    "ice",
    "and",
    "cream",
    "icecream",
    "man",
    "go",
    "mango",
]


@pytest.mark.parametrize(
    "s, words, expected",
    [
        (
            "ilikesamsungmobile",
            GFG_DICT,
            ["i like sam sung mobile", "i like samsung mobile"],
        ),
        (
            "ilikeicecreamandmango",
            GFG_DICT,
            [
                "i like ice cream and man go",
                "i like ice cream and mango",
                "i like icecream and man go",
                "i like icecream and mango",
            ],
        ),
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cat sand dog", "cats and dog"],
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"],
        ),
        (
            "aaaa",
            ["a", "aa"],
            ["a a a a", "a a aa", "a aa a", "aa a a", "aa aa"],
        ),  # words reused
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        ("abc", ["abc"], ["abc"]),
        ("abc", [], []),
    ],
)
def test_word_break(s, words, expected):
    assert sorted(word_break(s, words)) == sorted(expected)
