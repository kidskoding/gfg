import pytest
from helpers import load

is_interleaved = load("18_dynamic_programming.23_string_interleaving").is_interleaved


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        ("XXY", "XXZ", "XXZXXXY", False),
        ("XY", "WZ", "WZXY", True),
        ("XY", "X", "XXY", True),
        ("YX", "X", "XXY", False),
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("a", "b", "abc", False),  # length mismatch
        ("", "", "", True),
    ],
)
def test_is_interleaved(a, b, c, expected):
    assert is_interleaved(a, b, c) == expected
