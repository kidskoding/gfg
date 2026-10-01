import pytest
from helpers import load

remove_k_consecutive = load(
    "strings.37_repeatedly_remove_duplicates"
).remove_k_consecutive


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("geeksforgeeks", 2, "gksforgks"),
        ("qddxxxd", 3, "q"),
        ("deeedbbcccbdaa", 3, "aa"),
        ("pbbcggttciiippooaais", 2, "ps"),
        ("abbbaac", 3, "c"),  # removal exposes a new run
        ("abba", 2, ""),
        ("aaaaa", 2, "a"),
        ("aabbcc", 3, "aabbcc"),
        ("abc", 1, ""),
        ("", 2, ""),
    ],
)
def test_remove_k_consecutive(s, k, expected):
    assert remove_k_consecutive(s, k) == expected
