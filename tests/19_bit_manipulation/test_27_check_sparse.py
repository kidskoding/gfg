import pytest
from helpers import load

is_sparse = load("19_bit_manipulation.27_check_sparse").is_sparse


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (72, True),
        (5, True),
        (682, True),  # 1010101010
        (3, False),
        (12, False),
        (86, False),  # 1010110
        (1, True),
        (0, True),
    ],
)
def test_is_sparse(n, expected):
    assert is_sparse(n) is expected
