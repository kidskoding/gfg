import pytest
from helpers import load

edit_distance = load("18_dynamic_programming.03_edit_distance").edit_distance


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("geek", "gesek", 1),
        ("gfg", "gfg", 0),
        ("abcd", "bcfe", 3),
        ("sunday", "saturday", 3),
        ("kitten", "sitting", 3),
        ("", "abc", 3),
        ("abc", "", 3),
        ("", "", 0),
    ],
)
def test_edit_distance(s1, s2, expected):
    assert edit_distance(s1, s2) == expected
