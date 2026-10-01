import pytest
from helpers import load

huffman_codes = load("greedy.08_huffman_coding").huffman_codes


@pytest.mark.parametrize(
    "freq, expected_cost",
    [
        ({"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}, 224),
        ({"a": 1, "b": 2, "c": 4, "d": 8}, 25),  # skewed: codes of length 1, 2, 3, 3
        ({"a": 1, "b": 1, "c": 1, "d": 1}, 8),  # balanced: all length 2
        ({"a": 3, "b": 3, "c": 3}, 15),  # ties
        ({"a": 10, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1}, 27),
        ({"a": 1, "b": 1}, 2),
    ],
)
def test_huffman_codes(freq, expected_cost):
    codes = huffman_codes(freq)
    assert set(codes) == set(freq)
    words = list(codes.values())
    assert all(w and set(w) <= {"0", "1"} for w in words)
    for i, x in enumerate(words):
        for j, y in enumerate(words):
            assert i == j or not y.startswith(x), f"{x!r} is a prefix of {y!r}"
    assert sum(freq[s] * len(c) for s, c in codes.items()) == expected_cost


def test_huffman_single_symbol():
    assert huffman_codes({"x": 7}) == {"x": "0"}
