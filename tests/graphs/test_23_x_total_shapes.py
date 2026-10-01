import pytest
from helpers import load

count_x_shapes = load("graphs.23_x_total_shapes").count_x_shapes


@pytest.mark.parametrize(
    "rows, expected",
    [
        (["XOX", "OXO", "XXX"], 3),
        (["XX", "XX"], 1),
        (["XO", "OX"], 2),  # diagonals do not connect
        (["XOXOX"], 3),
        (["XXXOX", "OOXOX", "XOXXX"], 2),
        (["OO"], 0),
        (["X"], 1),
    ],
)
def test_count_x_shapes(rows, expected):
    assert count_x_shapes([list(row) for row in rows]) == expected
