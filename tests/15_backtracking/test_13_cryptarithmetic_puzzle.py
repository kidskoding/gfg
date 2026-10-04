import pytest
from helpers import load

solve_cryptarithmetic = load(
    "15_backtracking.13_cryptarithmetic_puzzle"
).solve_cryptarithmetic


def _value(word, mapping):
    return int("".join(str(mapping[ch]) for ch in word))


@pytest.mark.parametrize(
    "words, result",
    [
        (["SEND", "MORE"], "MONEY"),
        (["TWO", "TWO"], "FOUR"),
        (["BASE", "BALL"], "GAMES"),
        (["A", "A"], "B"),
        (["A", "B"], "A"),  # B = 0 is fine for a single-letter word
        (["A", "A"], "A"),  # forces A = 0
    ],
)
def test_solve_cryptarithmetic_found(words, result):
    mapping = solve_cryptarithmetic(words, result)
    assert mapping is not None
    assert set(mapping) == set("".join(words) + result)
    assert len(set(mapping.values())) == len(mapping)
    assert all(0 <= d <= 9 for d in mapping.values())
    assert all(mapping[w[0]] != 0 for w in [*words, result] if len(w) > 1)
    assert sum(_value(w, mapping) for w in words) == _value(result, mapping)


def test_send_more_money_is_unique():
    assert solve_cryptarithmetic(["SEND", "MORE"], "MONEY") == {
        "S": 9,
        "E": 5,
        "N": 6,
        "D": 7,
        "M": 1,
        "O": 0,
        "R": 8,
        "Y": 2,
    }


@pytest.mark.parametrize(
    "words, result",
    [
        (["X", "X"], "XX"),  # 2X = 11X forces X = 0, a leading zero
        (["A", "B"], "CDE"),  # two digits never sum to 100+
        (["AB", "CD", "EF"], "GHIJK"),  # 11 distinct letters
    ],
)
def test_solve_cryptarithmetic_none(words, result):
    assert solve_cryptarithmetic(words, result) is None
