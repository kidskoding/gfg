import pytest
from helpers import load

search_word = load("16_graphs.30_word_search").search_word


@pytest.mark.parametrize(
    "rows, word, expected",
    [
        (
            ["GEEKSFORGEEKS", "GEEKSQUIZGEEK", "IDEQAPRACTICE"],
            "GEEKS",
            [(0, 0), (0, 8), (1, 0)],
        ),
        (["abab", "abeb", "ebeb"], "abe", [(0, 0), (0, 2), (1, 0)]),
        (["aba"], "aba", [(0, 0), (0, 2)]),  # also reads right-to-left
        (["ab", "ba"], "a", [(0, 0), (1, 1)]),
        (["abc", "def"], "cfe", []),  # bends are not allowed
        (["ab"], "abc", []),
    ],
)
def test_search_word(rows, word, expected):
    assert search_word([list(row) for row in rows], word) == expected
