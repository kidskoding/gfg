import pytest
from helpers import load

number_to_words = load("strings.14_integer_to_words").number_to_words


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "Zero"),
        (5, "Five"),
        (13, "Thirteen"),
        (20, "Twenty"),
        (100, "One Hundred"),
        (123, "One Hundred Twenty Three"),
        (10245, "Ten Thousand Two Hundred Forty Five"),
        (90019, "Ninety Thousand Nineteen"),
        (1000000, "One Million"),
        (1000010, "One Million Ten"),
        (
            2147483647,
            (
                "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three"
                " Thousand Six Hundred Forty Seven"
            ),
        ),
    ],
)
def test_number_to_words(n, expected):
    assert number_to_words(n) == expected
