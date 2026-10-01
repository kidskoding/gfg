import pytest
from helpers import load

pattern_match = load("backtracking.18_pattern_match").pattern_match


@pytest.mark.parametrize(
    "pattern, s",
    [
        ("aba", "GraphTreesGraph"),
        ("GfG", "GeeksforGeeks"),
        ("abab", "redblueredblue"),
        ("aaaa", "asdasdasdasd"),
        ("ab", "xyz"),  # several valid answers
        ("a", "anything"),
        ("", ""),
    ],
)
def test_pattern_match_found(pattern, s):
    mapping = pattern_match(pattern, s)
    assert mapping is not None
    assert set(mapping) == set(pattern)
    assert all(mapping.values())
    assert len(set(mapping.values())) == len(mapping)
    assert "".join(mapping[ch] for ch in pattern) == s


@pytest.mark.parametrize(
    "pattern, s",
    [
        ("GG", "GeeksforGeeks"),
        ("aabb", "xyzabcxzyabc"),
        ("ab", "aa"),  # a and b would both need "a"
        ("abc", "xy"),  # every char needs a non-empty piece
        ("a", ""),
    ],
)
def test_pattern_match_none(pattern, s):
    assert pattern_match(pattern, s) is None
