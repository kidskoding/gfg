import pytest
from helpers import load

balanced_parentheses = load("recursion.30_balanced_parentheses").balanced_parentheses


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, [""]),
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ],
)
def test_balanced_parentheses(n, expected):
    assert sorted(balanced_parentheses(n)) == sorted(expected)


def _balanced(s):
    depth = 0
    for ch in s:
        depth += 1 if ch == "(" else -1
        if depth < 0:
            return False
    return depth == 0


@pytest.mark.parametrize("n, count", [(4, 14), (5, 42), (6, 132)])
def test_balanced_parentheses_counts(n, count):
    result = balanced_parentheses(n)
    assert len(result) == count
    assert len(set(result)) == count
    assert all(len(s) == 2 * n and _balanced(s) for s in result)
