import pytest
from helpers import load

longest_valid_parentheses = load(
    "02_strings.43_longest_valid_parentheses"
).longest_valid_parentheses


@pytest.mark.parametrize(
    "s, expected",
    [
        ("((()", 2),
        (")()())", 4),
        ("((()()", 4),
        ("()(())", 6),
        ("())(())", 4),
        ("((((", 0),
        (")(", 0),
        ("", 0),
    ],
)
def test_longest_valid_parentheses(s, expected):
    assert longest_valid_parentheses(s) == expected
