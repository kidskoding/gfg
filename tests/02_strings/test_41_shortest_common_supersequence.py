import pytest
from helpers import load

scs_length = load("02_strings.41_shortest_common_supersequence").scs_length


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("geek", "eke", 5),
        ("AGGTAB", "GXTXAYB", 9),
        ("abac", "cab", 5),
        ("abc", "abc", 3),
        ("abc", "def", 6),
        ("abc", "", 3),
        ("", "", 0),
    ],
)
def test_scs_length(a, b, expected):
    assert scs_length(a, b) == expected
