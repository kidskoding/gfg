import pytest
from helpers import load

BrowserHistory = load("stacks.34_browser_history").BrowserHistory


def _run(obj, ops):
    return [getattr(obj, name)(*args) for name, *args in ops]


@pytest.mark.parametrize(
    "args, ops, expected",
    [
        (
            ("leetcode.com",),
            [
                ("visit", "google.com"),
                ("visit", "facebook.com"),
                ("visit", "youtube.com"),
                ("back", 1),
                ("back", 1),
                ("forward", 1),
                ("visit", "linkedin.com"),
                ("forward", 2),
                ("back", 2),
                ("back", 7),
            ],
            [
                None,
                None,
                None,
                "facebook.com",
                "google.com",
                "facebook.com",
                None,
                "linkedin.com",
                "google.com",
                "leetcode.com",
            ],
        ),
        (
            ("a",),
            [
                ("back", 1),
                ("forward", 3),
                ("visit", "b"),
                ("back", 0),
                ("forward", 1),
                ("back", 5),
                ("visit", "c"),
                ("forward", 1),
                ("back", 1),
            ],
            ["a", "a", None, "b", "b", "a", None, "c", "a"],
        ),
        (
            ("x",),
            [
                ("visit", "y"),
                ("visit", "z"),
                ("back", 2),
                ("forward", 1),
                ("forward", 9),
            ],
            [None, None, "x", "y", "z"],
        ),
    ],
)
def test_browser_history(args, ops, expected):
    assert _run(BrowserHistory(*args), ops) == expected
