import pytest
from helpers import load

word_break_all = load("18_dynamic_programming.22_word_break_all_ways").word_break_all


@pytest.mark.parametrize(
    "s, words, expected",
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cat sand dog", "cats and dog"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"],
        ),
        ("aaa", ["a", "aa"], ["a a a", "a aa", "aa a"]),
        # duplicate dictionary words must not produce duplicate answers
        ("aa", ["a", "a", "aa"], ["a a", "aa"]),
        (
            "godisnowherenowhere",
            ["god", "is", "now", "no", "where", "here"],
            [
                "god is no where no where",
                "god is no where now here",
                "god is now here no where",
                "god is now here now here",
            ],
        ),
        ("abc", [], []),
        ("x", ["x"], ["x"]),
    ],
)
def test_word_break_all(s, words, expected):
    result = word_break_all(s, words)
    assert sorted(result) == sorted(expected)
