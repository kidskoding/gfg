import pytest
from helpers import load

postfix_to_prefix = load("stacks.03_postfix_to_prefix").postfix_to_prefix


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("AB+CD-*", "*+AB-CD"),
        ("ABC/-AK/L-*", "*-A/BC-/AKL"),
        ("ABC*+D+", "++A*BCD"),
        ("ab^c-", "-^abc"),
        ("AB+", "+AB"),
        ("A", "A"),
    ],
)
def test_postfix_to_prefix(expr, expected):
    assert postfix_to_prefix(expr) == expected
