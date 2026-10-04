import pytest
from helpers import load

lex_rank = load("02_strings.34_permutation_rank").lex_rank


@pytest.mark.parametrize(
    "s, expected",
    [
        ("acb", 2),
        ("string", 598),
        ("abc", 1),
        ("bac", 3),
        ("cba", 6),
        ("dcba", 24),
        ("a", 1),
    ],
)
def test_lex_rank(s, expected):
    assert lex_rank(s) == expected
