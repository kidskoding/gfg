import pytest
from helpers import load
from helpers.trees import build

height = load("trees.01_height_of_binary_tree").height


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([12, 8, 18, 5, 11], 2),
        ([1, 2, None, 3], 2),
        ([1, None, 2, None, 3, None, 4], 3),
        ([1], 0),
        ([], -1),
    ],
)
def test_height(tree, expected):
    assert height(build(tree)) == expected
