import pytest
from helpers import load

largest_swap = load("17_greedy.04_largest_number_one_swap").largest_swap


@pytest.mark.parametrize(
    "num, expected",
    [
        ("768", "867"),
        ("2736", "7236"),
        ("9937", "9973"),
        ("1993", "9913"),  # swap with the LAST occurrence of the max digit
        ("98368", "98863"),
        ("4321", "4321"),  # already largest: no swap
        ("333", "333"),
        ("5", "5"),
    ],
)
def test_largest_swap(num, expected):
    assert largest_swap(num) == expected
