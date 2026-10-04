import pytest
from helpers import load

longest_bracket_subsequence = load(
    "06_stacks.40_longest_bracket_subsequence_queries"
).longest_bracket_subsequence


@pytest.mark.parametrize(
    "s, queries, expected",
    [
        (
            "())(())(())(",
            [(0, 11), (1, 2), (2, 7), (3, 6), (7, 10), (5, 8), (0, 0)],
            [10, 0, 4, 4, 4, 0, 0],
        ),
        ("()()", [(0, 3), (1, 2), (0, 1)], [4, 0, 2]),
        (")(", [(0, 1)], [0]),
        ("((()))", [(0, 5), (1, 4), (0, 2)], [6, 4, 0]),
        ("", [], []),
    ],
)
def test_longest_bracket_subsequence(s, queries, expected):
    assert longest_bracket_subsequence(s, queries) == expected
