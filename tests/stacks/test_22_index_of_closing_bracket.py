import pytest
from helpers import load

closing_bracket_index = load("stacks.22_index_of_closing_bracket").closing_bracket_index


@pytest.mark.parametrize(
    "s, open_index, expected",
    [
        ("[ABC[23]][89]", 0, 8),
        ("[ABC[23]][89]", 4, 7),
        ("[ABC[23]][89]", 9, 12),
        ("[C-[D]]", 0, 6),
        ("[[]", 1, 2),
        ("[[]", 0, -1),
        ("[]", 1, -1),
        ("abc", 1, -1),
    ],
)
def test_closing_bracket_index(s, open_index, expected):
    assert closing_bracket_index(s, open_index) == expected
