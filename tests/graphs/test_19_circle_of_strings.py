import pytest
from helpers import load

can_form_circle = load("graphs.19_circle_of_strings").can_form_circle


@pytest.mark.parametrize(
    "words, expected",
    [
        (["geek", "king"], True),
        (["for", "geek", "rig", "kaf"], True),
        (["ab", "bc", "cd", "da"], True),
        (["ab", "ba", "ab", "ba"], True),  # duplicates
        (["aab", "abb"], False),
        (["aa", "bb"], False),  # balanced degrees but not connected
        (["ab", "bc", "ca", "xy"], False),
        (["aa"], True),
        (["ab"], False),
    ],
)
def test_can_form_circle(words, expected):
    assert can_form_circle(words) is expected
