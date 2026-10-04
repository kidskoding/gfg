import pytest
from helpers import load

remove_consecutive_same = load(
    "06_stacks.18_delete_consecutive_same_words"
).remove_consecutive_same


@pytest.mark.parametrize(
    "words, expected",
    [
        (["ab", "aa", "aa", "bcd", "ab"], ["ab", "bcd", "ab"]),
        (["tom", "jerry", "jerry", "tom"], []),
        (["a", "b", "b", "a", "c", "c", "d"], ["d"]),
        (["a", "a", "a"], ["a"]),
        (["x", "y", "z"], ["x", "y", "z"]),
        (["a"], ["a"]),
        ([], []),
    ],
)
def test_remove_consecutive_same(words, expected):
    assert remove_consecutive_same(words) == expected
