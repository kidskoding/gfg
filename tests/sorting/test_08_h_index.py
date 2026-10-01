import pytest
from helpers import load

h_index = load("sorting.08_h_index").h_index


@pytest.mark.parametrize(
    "citations, expected",
    [
        ([3, 0, 5, 3, 0], 3),
        ([5, 1, 2, 4, 1], 2),
        ([10, 8, 5, 4, 3], 4),
        ([4, 4, 4, 4], 4),
        ([1, 1, 1], 1),
        ([100], 1),
        ([0, 0], 0),
        ([], 0),
    ],
)
def test_h_index(citations, expected):
    assert h_index(citations) == expected
