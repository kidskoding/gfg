import pytest
from helpers import load

are_equivalent = load("stacks.30_equivalent_expressions").are_equivalent


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("-(a+b+c)", "-a-b-c", True),
        ("a-b-(c-d)", "a-b-c-d", False),
        ("a-(b-(c-d))", "a-b+c-d", True),
        ("(a-b)-(c+d)", "a-b-c-d", True),
        ("-(a-b)", "b-a", True),
        ("a+b", "b+a", True),
        ("a+b-a", "b", True),
        ("a+a", "a", False),
        ("a", "b", False),
    ],
)
def test_are_equivalent(a, b, expected):
    assert are_equivalent(a, b) == expected
