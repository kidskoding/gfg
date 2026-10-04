import pytest
from helpers import load

equal_point = load("02_strings.09_equal_point_brackets").equal_point


@pytest.mark.parametrize(
    "s, expected",
    [
        ("(())))(", 4),
        ("(()))(()", 4),
        ("()", 1),
        (")(", 1),
        ("))", 2),
        ("((", 0),
        ("", 0),
    ],
)
def test_equal_point(s, expected):
    assert equal_point(s) == expected
