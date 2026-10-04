import pytest
from helpers import load

first_circular_tour = load("07_queues.16_petrol_pump_tour").first_circular_tour


@pytest.mark.parametrize(
    "petrol, distance, expected",
    [
        ([4, 6, 7, 4], [6, 5, 3, 5], 1),
        ([6, 3, 7], [4, 6, 3], 2),
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),  # total petrol < total distance
        (
            [1, 1, 1],
            [1, 1, 1],
            0,
        ),  # every start works with an empty tank: smallest index
        ([0, 3, 3], [1, 1, 1], 1),  # starts 1 and 2 both work
        ([5], [5], 0),
        ([4], [5], -1),
        ([], [], -1),
    ],
)
def test_first_circular_tour(petrol, distance, expected):
    assert first_circular_tour(petrol, distance) == expected
