import pytest
from helpers import load

smallest_window_012 = load("sliding_window.02_smallest_window_012").smallest_window_012


@pytest.mark.parametrize(
    "s, expected",
    [
        ("10212", 3),
        ("12121", -1),  # no 0
        ("012", 3),
        ("000111222", 5),
        ("2101", 3),
        ("1102201", 3),
        ("0", -1),
        ("", -1),
    ],
)
def test_smallest_window_012(s, expected):
    assert smallest_window_012(s) == expected
