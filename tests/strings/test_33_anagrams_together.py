import pytest
from helpers import load

group_anagrams = load("strings.33_anagrams_together").group_anagrams


def _normalize(groups):
    return sorted(sorted(group) for group in groups)


@pytest.mark.parametrize(
    "words, expected",
    [
        (["act", "god", "cat", "dog", "tac"], [["act", "cat", "tac"], ["dog", "god"]]),
        (
            ["listen", "silent", "enlist", "abc", "cab", "bac", "rat"],
            [["abc", "bac", "cab"], ["enlist", "listen", "silent"], ["rat"]],
        ),
        (["ab", "ab", "ba"], [["ab", "ab", "ba"]]),  # duplicates kept
        (["abc", "abd"], [["abc"], ["abd"]]),
        (["", ""], [["", ""]]),
        (["a"], [["a"]]),
        ([], []),
    ],
)
def test_group_anagrams(words, expected):
    assert _normalize(group_anagrams(words)) == expected
