import pytest
from helpers import load

longest_valid_substring = load(
    "06_stacks.21_longest_valid_parentheses"
).longest_valid_substring


@pytest.mark.parametrize(
    "s, expected",
    [
        ("((()", 2),
        (")()())", 4),
        ("()(()))))", 6),
        ("(()())", 6),
        ("()(()", 2),
        ("()", 2),
        (")(", 0),
        ("(((", 0),
        ("", 0),
    ],
)
def test_longest_valid_substring(s, expected):
    assert longest_valid_substring(s) == expected
