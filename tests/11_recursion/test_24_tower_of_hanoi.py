import pytest
from helpers import load

tower_of_hanoi = load("11_recursion.24_tower_of_hanoi").tower_of_hanoi


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, [(1, "A", "C")]),
        (2, [(1, "A", "B"), (2, "A", "C"), (1, "B", "C")]),
        (
            3,
            [
                (1, "A", "C"),
                (2, "A", "B"),
                (1, "C", "B"),
                (3, "A", "C"),
                (1, "B", "A"),
                (2, "B", "C"),
                (1, "A", "C"),
            ],
        ),
    ],
)
def test_tower_of_hanoi(n, expected):
    assert [tuple(m) for m in tower_of_hanoi(n, "A", "C", "B")] == expected


def test_tower_of_hanoi_rod_names_respected():
    assert [tuple(m) for m in tower_of_hanoi(2, "X", "Y", "Z")] == [
        (1, "X", "Z"),
        (2, "X", "Y"),
        (1, "Z", "Y"),
    ]


@pytest.mark.parametrize("n", [1, 2, 4, 6, 8])
def test_tower_of_hanoi_simulates_legally(n):
    moves = tower_of_hanoi(n, "A", "C", "B")
    assert len(moves) == 2**n - 1
    rods = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    for disk, src, dst in moves:
        assert rods[src] and rods[src][-1] == disk
        assert not rods[dst] or rods[dst][-1] > disk
        rods[dst].append(rods[src].pop())
    assert rods == {"A": [], "B": [], "C": list(range(n, 0, -1))}
