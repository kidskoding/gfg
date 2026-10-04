import pytest
from helpers import load

matrix_chain_cost = load(
    "18_dynamic_programming.12_matrix_chain_multiplication"
).matrix_chain_cost


@pytest.mark.parametrize(
    "dims, expected",
    [
        ([2, 1, 3, 4], 20),
        ([1, 2, 3, 4, 3], 30),
        ([10, 20, 30, 40, 30], 30000),
        ([40, 20, 30, 10, 30], 26000),
        ([10, 20, 30], 6000),
        ([3, 4], 0),
    ],
)
def test_matrix_chain_cost(dims, expected):
    assert matrix_chain_cost(dims) == expected
