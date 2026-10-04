import pytest
from helpers import load

excel_column = load("02_strings.23_excel_column_name").excel_column


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "A"),
        (26, "Z"),
        (27, "AA"),
        (28, "AB"),
        (52, "AZ"),
        (53, "BA"),
        (702, "ZZ"),
        (703, "AAA"),
        (705, "AAC"),
    ],
)
def test_excel_column(n, expected):
    assert excel_column(n) == expected
