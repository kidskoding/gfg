import pytest
from helpers import load

case_sort = load("09_sorting.18_case_specific_sort").case_sort


@pytest.mark.parametrize(
    "s, expected",
    [
        ("defRTSersUXI", "deeIRSfrsTUX"),
        ("srbDKi", "birDKs"),
        ("BaAb", "AaBb"),
        ("zyx", "xyz"),
        ("QWE", "EQW"),
        ("a", "a"),
        ("", ""),
    ],
)
def test_case_sort(s, expected):
    assert case_sort(s) == expected
