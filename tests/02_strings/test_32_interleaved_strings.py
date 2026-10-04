import pytest
from helpers import load

is_interleave = load("02_strings.32_interleaved_strings").is_interleave


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        ("XY", "WZ", "WZXY", True),
        ("XY", "X", "XXY", True),
        ("YX", "X", "XXY", False),  # Y must precede X
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("XXY", "XXZ", "XXZXXXY", False),
        ("a", "b", "abc", False),  # length mismatch
        ("a", "", "a", True),
        ("", "", "", True),
    ],
)
def test_is_interleave(a, b, c, expected):
    assert is_interleave(a, b, c) is expected
