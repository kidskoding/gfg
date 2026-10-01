import pytest
from helpers import load

generate_binary = load("queues.03_generate_binary_numbers").generate_binary


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, ["1", "10"]),
        (5, ["1", "10", "11", "100", "101"]),
        (8, ["1", "10", "11", "100", "101", "110", "111", "1000"]),
        (1, ["1"]),
        (0, []),
        (-3, []),
    ],
)
def test_generate_binary(n, expected):
    assert generate_binary(n) == expected


def test_generate_binary_large():
    out = generate_binary(1000)
    assert len(out) == 1000
    assert out[-1] == "1111101000"
    assert all(int(s, 2) == i for i, s in enumerate(out, start=1))
