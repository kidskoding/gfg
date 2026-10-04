import pytest
from helpers import load

mod = load("11_recursion.22_pyramid_patterns")
star_triangle = mod.star_triangle
full_pyramid = mod.full_pyramid


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, ["*", "* *", "* * *", "* * * *", "* * * * *"]),
        (3, ["*", "* *", "* * *"]),
        (1, ["*"]),
        (2, ["*", "* *"]),
        (0, []),
    ],
)
def test_star_triangle(n, expected):
    assert star_triangle(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, ["    *", "   * *", "  * * *", " * * * *", "* * * * *"]),
        (3, ["  *", " * *", "* * *"]),
        (1, ["*"]),
        (2, [" *", "* *"]),
        (0, []),
    ],
)
def test_full_pyramid(n, expected):
    assert full_pyramid(n) == expected
