import pytest
from helpers import load

scs_length = load("18_dynamic_programming.11_shortest_common_supersequence").scs_length


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("geek", "eke", 5),
        ("AGGTAB", "GXTXAYB", 9),
        ("abc", "abc", 3),
        ("abc", "def", 6),
        ("abc", "", 3),
        ("", "", 0),
    ],
)
def test_scs_length(s1, s2, expected):
    assert scs_length(s1, s2) == expected
