import pytest
from helpers import load

remove_adjacent_duplicates = load(
    "11_recursion.17_remove_adjacent_duplicates"
).remove_adjacent_duplicates


@pytest.mark.parametrize(
    "s, expected",
    [
        ("geeksforgeeg", "gksfor"),
        ("azxxzy", "ay"),
        ("caaabbbaac", ""),
        ("gghhg", "g"),
        ("aaaacddddcappp", "a"),
        ("acaaabbbacdddd", "acac"),
        ("aaa", ""),  # whole run goes, not just a pair
        ("abc", "abc"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_remove_adjacent_duplicates(s, expected):
    assert remove_adjacent_duplicates(s) == expected
