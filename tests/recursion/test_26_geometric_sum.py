import pytest
from helpers import load

geometric_sum = load("recursion.26_geometric_sum").geometric_sum


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1.0),
        (1, 4 / 3),
        (2, 13 / 9),
        (3, 40 / 27),
        (5, 1.4979424),
        (30, 1.5),
    ],
)
def test_geometric_sum(n, expected):
    assert geometric_sum(n) == pytest.approx(expected, rel=1e-7)
