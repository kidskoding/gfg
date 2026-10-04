import pytest
from helpers import load
from helpers.trees import build

k_distance = load("13_trees.08_nodes_at_given_distance").k_distance


@pytest.mark.parametrize(
    "k, expected",
    [(0, [1]), (1, [2, 3]), (2, [4, 5, 6]), (3, []), (5, [])],
)
def test_k_distance(k, expected):
    assert k_distance(build([1, 2, 3, 4, 5, None, 6]), k) == expected
