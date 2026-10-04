import pytest
from helpers import load

has_permutation_substring = load(
    "05_sliding_window.03_permutation_in_string"
).has_permutation_substring


@pytest.mark.parametrize(
    "txt, pat, expected",
    [
        ("geeks", "eke", True),
        ("programming", "rain", False),
        ("cbaebabacd", "abc", True),
        ("aaab", "aab", True),
        ("abcd", "dd", False),  # duplicates in pat must be matched
        ("ab", "abc", False),  # pat longer than txt
        ("a", "a", True),
    ],
)
def test_has_permutation_substring(txt, pat, expected):
    assert has_permutation_substring(txt, pat) == expected
