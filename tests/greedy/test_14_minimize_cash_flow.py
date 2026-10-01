import pytest
from helpers import load

minimize_cash_flow = load("greedy.14_minimize_cash_flow").minimize_cash_flow


def _net(graph):
    n = len(graph)
    return [sum(graph[j][i] for j in range(n)) - sum(graph[i]) for i in range(n)]


@pytest.mark.parametrize(
    "graph, max_payments",
    [
        ([[0, 1000, 2000], [0, 0, 5000], [0, 0, 0]], 2),
        ([[0, 10, 0, 0], [0, 0, 20, 0], [0, 0, 0, 30], [40, 0, 0, 0]], 3),
        ([[0, 50], [0, 0]], 1),
        ([[0, 30, 0, 0], [0, 0, 0, 0], [0, 0, 0, 30], [0, 0, 0, 0]], 3),
        ([[0, 10, 0], [0, 0, 10], [10, 0, 0]], 0),  # cycle cancels out
        ([[0, 100], [100, 0]], 0),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
        ([[0]], 0),
    ],
)
def test_minimize_cash_flow(graph, max_payments):
    balance = _net(graph)
    payments = [tuple(p) for p in minimize_cash_flow(graph)]
    for payer, payee, amount in payments:
        assert amount > 0
        balance[payer] += amount
        balance[payee] -= amount
    assert balance == [0] * len(graph)
    payers = {p for p, _, _ in payments}
    payees = {q for _, q, _ in payments}
    assert not payers & payees
    assert len(payments) <= max_payments
