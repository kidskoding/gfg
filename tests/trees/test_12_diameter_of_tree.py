import pytest
from helpers import load
from helpers.trees import build

diameter = load("trees.12_diameter_of_tree").diameter


@pytest.mark.parametrize(
    "tree, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, None, 3, None, 4], 3),
        ([1, 2, None, 3, 4, 5, None, 8, None, 6, None, 9], 6),  # path avoids root
        ([1], 0),
        ([], 0),
    ],
)
def test_diameter(tree, expected):
    assert diameter(build(tree)) == expected
