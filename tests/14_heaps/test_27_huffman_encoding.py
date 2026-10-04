import pytest
from helpers import load

huffman_codes = load("14_heaps.27_huffman_encoding").huffman_codes


@pytest.mark.parametrize(
    "chars, freq, optimal_cost",
    [
        ("abcdef", [5, 9, 12, 13, 16, 45], 224),
        ("abcde", [10, 1, 1, 1, 1], 22),
        ("abcd", [1, 1, 1, 1], 8),
        ("abc", [1, 1, 2], 6),
        ("ab", [1, 1], 2),
        ("a", [5], 5),
    ],
)
def test_huffman_codes(chars, freq, optimal_cost):
    codes = huffman_codes(chars, freq)
    assert set(codes) == set(chars)
    words = list(codes.values())
    assert all(w and set(w) <= {"0", "1"} for w in words)
    assert not any(
        a != b and b.startswith(a) for a in words for b in words
    )  # prefix-free
    assert len(set(words)) == len(words)
    assert sum(f * len(codes[c]) for c, f in zip(chars, freq)) == optimal_cost


def test_huffman_single_char_gets_zero():
    assert huffman_codes("z", [3]) == {"z": "0"}
