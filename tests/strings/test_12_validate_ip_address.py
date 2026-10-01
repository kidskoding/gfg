import pytest
from helpers import load

is_valid_ipv4 = load("strings.12_validate_ip_address").is_valid_ipv4


@pytest.mark.parametrize(
    "s, expected",
    [
        ("128.0.0.1", True),
        ("125.16.100.1", True),
        ("0.0.0.0", True),
        ("255.255.255.255", True),
        ("256.0.0.1", False),  # out of range
        ("125.512.100.abc", False),
        ("01.2.3.4", False),  # leading zero
        ("1.2.3", False),
        ("1.2.3.4.5", False),
        ("1..2.3", False),
        ("1.2.3.4.", False),
        ("1.2.3.-4", False),
        ("", False),
    ],
)
def test_is_valid_ipv4(s, expected):
    assert is_valid_ipv4(s) is expected
