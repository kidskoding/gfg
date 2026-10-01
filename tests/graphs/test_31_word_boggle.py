import pytest
from helpers import load

word_boggle = load("graphs.31_word_boggle").word_boggle


@pytest.mark.parametrize(
    "rows, dictionary, expected",
    [
        (["GIZ", "UEK", "QSE"], ["GEEKS", "FOR", "QUIZ", "GO"], ["GEEKS", "QUIZ"]),
        (["CAP", "AND", "TIE"], ["CAT"], ["CAT"]),
        (["AB"], ["ABA", "AB", "BA"], ["AB", "BA"]),  # no cell reused
        (["AA"], ["AA", "AAA"], ["AA"]),
        (["AB", "CD"], ["AD", "BC", "ACDB", "ABDCA"], ["ACDB", "AD", "BC"]),
        (["AB"], ["AB", "AB"], ["AB"]),  # duplicates in dictionary
        (["X"], ["Y"], []),
    ],
)
def test_word_boggle(rows, dictionary, expected):
    assert word_boggle([list(row) for row in rows], dictionary) == expected
