import pytest
from helpers import load

catch_thieves = load("greedy.12_policemen_catch_thieves").catch_thieves


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        (["P", "T", "T", "P", "T"], 1, 2),
        (["T", "T", "P", "P", "T", "P"], 2, 3),
        (["P", "T", "P", "T", "T", "P"], 3, 3),
        (["T", "P", "T", "P"], 1, 2),
        (["P", "T", "T", "T", "P"], 1, 2),
        (["P", "T"], 0, 0),  # nobody in reach
        (["P", "P", "P"], 1, 0),  # no thieves
        (["T", "T"], 5, 0),  # no policemen
        ([], 1, 0),
    ],
)
def test_catch_thieves(arr, k, expected):
    assert catch_thieves(arr, k) == expected
