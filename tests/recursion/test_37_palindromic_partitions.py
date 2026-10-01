import pytest
from helpers import load

palindromic_partitions = load(
    "recursion.37_palindromic_partitions"
).palindromic_partitions


def _norm(parts):
    return sorted(tuple(p) for p in parts)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("nitin", [["n", "i", "t", "i", "n"], ["n", "iti", "n"], ["nitin"]]),
        ("geeks", [["g", "e", "e", "k", "s"], ["g", "ee", "k", "s"]]),
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
        ("abc", [["a", "b", "c"]]),
        ("a", [["a"]]),
        ("", [[]]),
    ],
)
def test_palindromic_partitions(s, expected):
    assert _norm(palindromic_partitions(s)) == _norm(expected)


def test_palindromic_partitions_count():
    result = palindromic_partitions("aaaaaa")
    assert len(result) == 32  # every one of the 5 gaps can be cut or not
    assert all("".join(p) == "aaaaaa" for p in result)
