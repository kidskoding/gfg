import pytest
from helpers import load

decimal_to_binary = load("11_recursion.05_decimal_to_binary").decimal_to_binary


@pytest.mark.parametrize(
    "n, expected",
    [
        (7, "111"),
        (10, "1010"),
        (33, "100001"),
        (1, "1"),
        (0, "0"),
        (2, "10"),
        (255, "11111111"),
        (1024, "10000000000"),
    ],
)
def test_decimal_to_binary(n, expected):
    assert decimal_to_binary(n) == expected
