import pytest
from helpers import load

replace_surrounded = load("16_graphs.08_replace_os_with_xs").replace_surrounded


def _grid(rows):
    return [list(row) for row in rows]


@pytest.mark.parametrize(
    "rows, expected",
    [
        (
            ["XXXX", "XOXX", "XOOX", "XOXX", "XXOO"],
            ["XXXX", "XXXX", "XXXX", "XXXX", "XXOO"],
        ),
        (["XXXX", "XOOX", "XXOX", "XOXX"], ["XXXX", "XXXX", "XXXX", "XOXX"]),
        (["XXX", "XOX", "XXX"], ["XXX", "XXX", "XXX"]),
        (["XOX", "XOX", "XXX"], ["XOX", "XOX", "XXX"]),  # reaches the border
        (["OO", "OO"], ["OO", "OO"]),
        (["XXXXX", "XOXOX", "XXXXX"], ["XXXXX", "XXXXX", "XXXXX"]),
        (["O"], ["O"]),
    ],
)
def test_replace_surrounded(rows, expected):
    grid = _grid(rows)
    assert replace_surrounded(grid) is None
    assert grid == _grid(expected)
