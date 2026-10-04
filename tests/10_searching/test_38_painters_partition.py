import pytest
from helpers import load

painters_partition = load("10_searching.38_painters_partition").painters_partition


@pytest.mark.parametrize(
    "boards, k, expected",
    [
        ([5, 10, 30, 20, 15], 3, 35),
        ([10, 20, 30, 40], 2, 60),
        ([7, 2, 5, 10, 8], 2, 18),
        ([5, 5, 5, 5], 2, 10),
        ([1, 2, 3, 4, 5], 1, 15),
        ([10, 20], 5, 20),  # more painters than boards
        ([100], 1, 100),
    ],
)
def test_painters_partition(boards, k, expected):
    assert painters_partition(boards, k) == expected
