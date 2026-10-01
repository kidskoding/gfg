import pytest
from helpers import load

can_finish = load("graphs.17_prerequisite_tasks").can_finish


@pytest.mark.parametrize(
    "n, prerequisites, expected",
    [
        (4, [(1, 0), (2, 1), (3, 2)], True),
        (2, [(1, 0), (0, 1)], False),
        (4, [(1, 0), (2, 1), (3, 2), (1, 3)], False),
        (5, [(1, 0), (2, 0), (3, 1), (3, 2), (4, 3)], True),
        (2, [(0, 0)], False),  # task depends on itself
        (3, [], True),
        (1, [], True),
    ],
)
def test_can_finish(n, prerequisites, expected):
    assert can_finish(n, prerequisites) is expected
