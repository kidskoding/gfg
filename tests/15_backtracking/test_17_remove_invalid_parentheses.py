import pytest
from helpers import load

remove_invalid_parentheses = load(
    "15_backtracking.17_remove_invalid_parentheses"
).remove_invalid_parentheses


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()())()", ["(())()", "()()()"]),
        ("(a)())()", ["(a())()", "(a)()()"]),
        (")(", [""]),
        ("(()", ["()"]),
        (")o(v(", ["ov"]),
        ("()", ["()"]),  # already valid
        ("abc", ["abc"]),  # no parentheses at all
        ("", [""]),
    ],
)
def test_remove_invalid_parentheses(s, expected):
    assert remove_invalid_parentheses(s) == expected
