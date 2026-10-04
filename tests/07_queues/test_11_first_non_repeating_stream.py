import pytest
from helpers import load

first_non_repeating = load("07_queues.11_first_non_repeating_stream").first_non_repeating


@pytest.mark.parametrize(
    "stream, expected",
    [
        ("aabc", "a#bb"),
        ("zz", "z#"),
        ("abcabc", "aaabc#"),
        ("aabbcc", "a#b#c#"),
        ("abba", "aaa#"),
        ("aaab", "a##b"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_first_non_repeating(stream, expected):
    assert first_non_repeating(stream) == expected
