import pytest
from helpers import load

min_time_to_finish = load("17_greedy.15_min_time_finish_jobs").min_time_to_finish


@pytest.mark.parametrize(
    "jobs, k, t, expected",
    [
        ([4, 5, 10], 2, 5, 50),
        ([10, 7, 8, 12, 6, 8], 4, 5, 75),
        ([7, 2, 5, 10, 8], 2, 1, 18),
        ([1, 1, 1, 1], 2, 4, 8),
        ([1, 2, 3, 4, 5], 1, 1, 15),  # one assignee does everything
        ([1, 2, 3, 4, 5], 10, 2, 10),  # more assignees than jobs
        ([5], 1, 3, 15),
        ([], 3, 2, 0),
    ],
)
def test_min_time_to_finish(jobs, k, t, expected):
    assert min_time_to_finish(jobs, k, t) == expected
