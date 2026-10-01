import pytest
from helpers import load
from helpers.trees import build

zigzag = load("trees.17_zigzag_traversal").zigzag


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 4, 5, 6, 7]),
        ([7, 9, 7, 8, 8, 6, None, 10, 9], [7, 7, 9, 8, 8, 6, 9, 10]),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [1, 3, 2, 4, 5, 6, 7, 15, 14, 13, 12, 11, 10, 9, 8],
        ),
        ([1, 2, 3, 4, None, None, 5], [1, 3, 2, 4, 5]),
        ([1, 2, 3, None, None, 4, 5, 6, None, None, 7], [1, 3, 2, 4, 5, 7, 6]),
        ([1, 2], [1, 2]),
        ([1, None, 2], [1, 2]),
        ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),  # one node per level: order unaffected
        ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),
        ([1], [1]),
        ([], []),
    ],
)
def test_zigzag(tree, expected):
    assert zigzag(build(tree)) == expected
