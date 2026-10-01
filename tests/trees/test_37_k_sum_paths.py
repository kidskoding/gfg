import pytest
from helpers import load
from helpers.trees import build

k_sum_paths = load("trees.37_k_sum_paths").k_sum_paths


@pytest.mark.parametrize(
    "tree, k, expected",
    [
        ([1, 2, 3], 3, 2),
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([1, -1, 1, None, None, None, -1], 0, 2),
        ([1, 1, 1, 1], 2, 3),
        ([5], 5, 1),
        ([], 0, 0),
    ],
)
def test_k_sum_paths(tree, k, expected):
    assert k_sum_paths(build(tree), k) == expected
