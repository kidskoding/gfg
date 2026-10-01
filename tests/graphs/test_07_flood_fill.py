import pytest
from helpers import load

flood_fill = load("graphs.07_flood_fill").flood_fill


@pytest.mark.parametrize(
    "image, sr, sc, new_color, expected",
    [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 1, 1]], 0, 0, 2, [[2, 2, 2], [2, 1, 1]]),
        ([[0, 0, 0], [0, 1, 1]], 1, 1, 7, [[0, 0, 0], [0, 7, 7]]),
        ([[1, 0], [0, 1]], 0, 0, 9, [[9, 0], [0, 1]]),  # diagonal is not connected
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),  # same colour
        ([[5]], 0, 0, 3, [[3]]),
    ],
)
def test_flood_fill(image, sr, sc, new_color, expected):
    result = flood_fill(image, sr, sc, new_color)
    assert result is image
    assert image == expected
