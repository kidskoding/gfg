import pytest
from helpers import load

ladder_length = load("graphs.39_word_ladder_i").ladder_length


@pytest.mark.parametrize(
    "begin, end, word_list, expected",
    [
        ("toon", "plea", ["poon", "plee", "same", "poie", "plie", "poin", "plea"], 7),
        ("abcv", "ebad", ["abcd", "ebad", "ebcd", "xyza"], 4),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),  # end not in list
        ("hit", "hot", ["hot"], 2),
        ("a", "c", ["a", "b", "c"], 2),
        ("abc", "xyz", ["xyz"], 0),
    ],
)
def test_ladder_length(begin, end, word_list, expected):
    assert ladder_length(begin, end, word_list) == expected
