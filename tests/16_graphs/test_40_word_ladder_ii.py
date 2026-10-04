import pytest
from helpers import load

find_ladders = load("16_graphs.40_word_ladder_ii").find_ladders


@pytest.mark.parametrize(
    "begin, end, word_list, expected",
    [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
        ),
        (
            "der",
            "dfs",
            ["des", "der", "dfr", "dgt", "dfs"],
            [["der", "des", "dfs"], ["der", "dfr", "dfs"]],
        ),
        (
            "abcv",
            "ebad",
            ["abcd", "ebad", "ebcd", "xyza"],
            [["abcv", "abcd", "ebcd", "ebad"]],
        ),
        ("a", "c", ["a", "b", "c"], [["a", "c"]]),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
        ("abc", "xyz", ["xyz"], []),
    ],
)
def test_find_ladders(begin, end, word_list, expected):
    assert sorted(find_ladders(begin, end, word_list)) == expected
