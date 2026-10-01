import pytest
from helpers import load

job_sequencing = load("greedy.03_job_sequencing").job_sequencing


@pytest.mark.parametrize(
    "deadline, profit, expected",
    [
        ([4, 1, 1, 1], [20, 10, 40, 30], (2, 60)),
        ([2, 1, 2, 1, 1], [100, 19, 27, 25, 15], (2, 127)),
        ([3, 1, 2, 2], [50, 10, 20, 30], (3, 100)),
        ([2, 2, 1, 3, 3], [10, 20, 30, 5, 40], (3, 90)),
        ([1, 1, 1], [5, 5, 5], (1, 5)),  # all compete for one slot
        ([5, 5, 5], [1, 2, 3], (3, 6)),  # room for everything
        ([1], [5], (1, 5)),
        ([], [], (0, 0)),
    ],
)
def test_job_sequencing(deadline, profit, expected):
    assert tuple(job_sequencing(deadline, profit)) == expected
