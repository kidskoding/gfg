import pytest
from helpers import load

encrypt = load("02_strings.08_encrypt_the_string").encrypt


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aaaaaaaaaaa", "ba"),  # a11 -> ab -> ba
        ("abc", "1c1b1a"),
        ("aabccc", "3c1b2a"),
        ("a", "1a"),
        ("a" * 16, "01a"),  # a10
        ("a" * 17 + "b", "1b11a"),  # a11b1
        ("z" * 255, "ffz"),  # zff
    ],
)
def test_encrypt(s, expected):
    assert encrypt(s) == expected
