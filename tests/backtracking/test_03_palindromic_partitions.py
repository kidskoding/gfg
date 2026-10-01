import pytest
from helpers import load

palindromic_partitions = load(
    "backtracking.03_palindromic_partitions"
).palindromic_partitions


@pytest.mark.parametrize(
    "s, expected",
    [
        ("nitin", [["n", "i", "t", "i", "n"], ["n", "iti", "n"], ["nitin"]]),
        ("geeks", [["g", "e", "e", "k", "s"], ["g", "ee", "k", "s"]]),
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
        ("abc", [["a", "b", "c"]]),
        ("abba", [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]),
        ("a", [["a"]]),
    ],
)
def test_palindromic_partitions(s, expected):
    assert sorted(palindromic_partitions(s)) == sorted(expected)
