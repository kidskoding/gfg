import pytest
from helpers import load

is_balanced = load("06_stacks.01_parenthesis_checker").is_balanced


@pytest.mark.parametrize(
    "s, expected",
    [
        ("[()]{}{[()()]()}", True),
        ("[(])", False),
        ("()", True),
        ("((()))[]", True),
        ("{[}]", False),
        ("(", False),
        (")", False),
        ("]]", False),
        ("", True),
    ],
)
def test_is_balanced(s, expected):
    assert is_balanced(s) == expected
