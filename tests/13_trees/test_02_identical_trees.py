import pytest
from helpers import load
from helpers.trees import build

is_identical = load("13_trees.02_identical_trees").is_identical


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 3], [1, 3, 2], False),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 3], [1, 2], False),
        ([], [], True),
        ([1], [], False),
    ],
)
def test_is_identical(a, b, expected):
    assert is_identical(build(a), build(b)) is expected
