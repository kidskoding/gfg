import pytest
from helpers import load

look_and_say = load("02_strings.21_look_and_say").look_and_say


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "1"),
        (2, "11"),
        (3, "21"),
        (4, "1211"),
        (5, "111221"),
        (6, "312211"),
        (7, "13112221"),
        (8, "1113213211"),
    ],
)
def test_look_and_say(n, expected):
    assert look_and_say(n) == expected
