import pytest
from helpers import load
from helpers.trees import build

count_turns = load("trees.38_number_of_turns").count_turns


@pytest.mark.parametrize(
    "a, b, expected",
    [(5, 6, 3), (1, 4, -1), (4, 5, 1), (2, 7, 1), (8, 4, 2), (1, 8, 2), (8, 9, 5), (4, 8, 2)],
)
def test_count_turns(a, b, expected):
    root = build([1, 2, 3, 4, 5, 6, 7, None, None, 8, None, None, 9])
    assert count_turns(root, a, b) == expected
