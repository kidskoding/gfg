import pytest
from helpers import load

flood_fill = load("recursion.35_flood_fill").flood_fill


@pytest.mark.parametrize(
    "image, sr, sc, new_color, expected",
    [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 1, 1]], 1, 1, 2, [[0, 0, 0], [0, 2, 2]]),
        (
            [[0, 0, 0], [0, 1, 1]],
            1,
            1,
            1,
            [[0, 0, 0], [0, 1, 1]],
        ),  # same color: unchanged
        ([[1, 0], [0, 1]], 0, 0, 3, [[3, 0], [0, 1]]),  # diagonals are not connected
        ([[5]], 0, 0, 9, [[9]]),
        ([[4, 4], [4, 4]], 1, 0, 7, [[7, 7], [7, 7]]),
        (
            [[1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0]],
            0,
            0,
            8,
            [[8, 8, 0, 8], [0, 8, 0, 8], [8, 8, 8, 8], [0, 0, 0, 0]],
        ),
    ],
)
def test_flood_fill(image, sr, sc, new_color, expected):
    result = flood_fill(image, sr, sc, new_color)
    assert result is image
    assert image == expected
