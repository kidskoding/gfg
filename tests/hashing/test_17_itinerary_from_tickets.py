import pytest
from helpers import load

find_itinerary = load("hashing.17_itinerary_from_tickets").find_itinerary


@pytest.mark.parametrize(
    "tickets, expected",
    [
        (
            [
                ("Chennai", "Banglore"),
                ("Bombay", "Delhi"),
                ("Goa", "Chennai"),
                ("Delhi", "Goa"),
            ],
            ["Bombay", "Delhi", "Goa", "Chennai", "Banglore"],
        ),
        ([("A", "B")], ["A", "B"]),
        ([("B", "C"), ("A", "B")], ["A", "B", "C"]),
        ([("C", "D"), ("B", "C"), ("D", "E"), ("A", "B")], ["A", "B", "C", "D", "E"]),
        ([("x", "y"), ("w", "x"), ("y", "z")], ["w", "x", "y", "z"]),
        ([], []),
    ],
)
def test_find_itinerary(tickets, expected):
    assert find_itinerary(tickets) == expected
