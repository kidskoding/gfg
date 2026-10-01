import pytest
from helpers import load

is_pangram = load("strings.11_pangram_check").is_pangram


@pytest.mark.parametrize(
    "s, expected",
    [
        ("The quick brown fox jumps over the lazy dog", True),
        ("Pack my box with five dozen liquor jugs!", True),
        ("The quick brown fox jumps over the dog", False),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
        ("abcdefghijklmnopqrstuvwxy", False),  # missing z
        ("", False),
    ],
)
def test_is_pangram(s, expected):
    assert is_pangram(s) is expected
