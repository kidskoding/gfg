import pytest
from helpers import load

has_hamiltonian_path = load("graphs.44_hamiltonian_path").has_hamiltonian_path


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (4, [(0, 1), (1, 2), (2, 3), (1, 3)], True),
        (4, [(0, 1), (1, 2), (1, 3)], False),  # star
        (5, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4)], True),
        (4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], True),
        (4, [(0, 1), (2, 3)], False),  # disconnected
        (3, [(0, 1), (1, 2)], True),
        (2, [], False),
        (1, [], True),
    ],
)
def test_has_hamiltonian_path(n, edges, expected):
    assert has_hamiltonian_path(n, edges) is expected
