import pytest
from helpers import load

max_product_cut = load(
    "dynamic_programming.17_max_product_cutting_rope"
).max_product_cut


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 6),
        (8, 18),
        (10, 36),
    ],
)
def test_max_product_cut(n, expected):
    assert max_product_cut(n) == expected
