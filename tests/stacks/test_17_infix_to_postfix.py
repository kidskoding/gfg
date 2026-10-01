import pytest
from helpers import load

infix_to_postfix = load("stacks.17_infix_to_postfix").infix_to_postfix


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("a+b*(c^d-e)^(f+g*h)-i", "abcd^e-fgh*+^*+i-"),
        ("A*(B+C)/D", "ABC+*D/"),
        ("a+b*c-d/e", "abc*+de/-"),
        ("(a+b)*(c-d)", "ab+cd-*"),
        ("a-b-c", "ab-c-"),
        ("a^b^c", "abc^^"),
        ("a+b", "ab+"),
        ("a", "a"),
    ],
)
def test_infix_to_postfix(expr, expected):
    assert infix_to_postfix(expr) == expected
