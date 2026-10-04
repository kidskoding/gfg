import pytest
from helpers import load

evaluate_postfix = load("06_stacks.10_evaluate_postfix").evaluate_postfix


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "3", "1", "*", "+", "9", "-"], -4),
        (["100", "200", "+", "2", "/", "5", "*", "7", "+"], 757),
        (["4", "13", "5", "/", "+"], 6),
        (["2", "3", "^"], 8),
        (["2", "3", "2", "^", "^"], 512),
        (["-3", "4", "*"], -12),
        (["7", "2", "/"], 3),
        (["-7", "2", "/"], -4),
        (["5"], 5),
    ],
)
def test_evaluate_postfix(tokens, expected):
    assert evaluate_postfix(tokens) == expected
