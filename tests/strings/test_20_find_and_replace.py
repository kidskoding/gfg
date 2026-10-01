import pytest
from helpers import load

replace_all = load("strings.20_find_and_replace").replace_all


@pytest.mark.parametrize(
    "s, old, new, expected",
    [
        ("abababa", "aba", "a", "aba"),
        ("geeksforgeeks", "eek", "ok", "goksforgoks"),
        ("abc", "b", "xyz", "axyzc"),
        ("aaaa", "aa", "b", "bb"),
        ("aaa", "aa", "b", "ba"),  # non-overlapping, left to right
        ("hello", "xyz", "a", "hello"),
        ("abc", "abc", "", ""),
    ],
)
def test_replace_all(s, old, new, expected):
    assert replace_all(s, old, new) == expected
