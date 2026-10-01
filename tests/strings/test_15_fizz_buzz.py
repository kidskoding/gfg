import pytest
from helpers import load

fizz_buzz = load("strings.15_fizz_buzz").fizz_buzz


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, ["1"]),
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
            + ["11", "Fizz", "13", "14", "FizzBuzz"],
        ),
        (0, []),
    ],
)
def test_fizz_buzz(n, expected):
    assert fizz_buzz(n) == expected
