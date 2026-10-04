import pytest
from helpers import load

count_true_ways = load(
    "18_dynamic_programming.10_boolean_parenthesization"
).count_true_ways


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("T|T&F^T", 4),
        ("T^F|F", 2),
        ("T^F&T", 2),
        ("T|F", 1),
        ("T&F", 0),
        ("T", 1),
        ("F", 0),
    ],
)
def test_count_true_ways(expr, expected):
    assert count_true_ways(expr) == expected
