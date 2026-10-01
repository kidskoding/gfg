from itertools import pairwise

import pytest
from helpers import load

rearrange_characters = load("heaps.09_rearrange_characters").rearrange_characters


@pytest.mark.parametrize(
    "s, possible",
    [
        ("aaabc", True),
        ("aaabb", True),
        ("aab", True),
        ("abcabc", True),
        ("bbbbaaac", True),
        ("aa", False),
        ("aaab", False),
        ("a", True),
        ("", True),
    ],
)
def test_rearrange_characters(s, possible):
    result = rearrange_characters(s)
    if possible:
        assert sorted(result) == sorted(s)
        assert all(a != b for a, b in pairwise(result))
    else:
        assert result == ""
