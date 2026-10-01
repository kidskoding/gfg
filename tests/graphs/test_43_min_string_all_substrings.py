from itertools import product

import pytest
from helpers import load

min_string_with_all_substrings = load(
    "graphs.43_min_string_all_substrings"
).min_string_with_all_substrings


@pytest.mark.parametrize(
    "n, k",
    [(1, 1), (1, 5), (2, 1), (2, 2), (3, 2), (2, 3), (3, 3), (4, 2)],
)
def test_min_string_with_all_substrings(n, k):
    s = min_string_with_all_substrings(n, k)
    assert len(s) == k**n + n - 1
    assert set(s) <= {str(d) for d in range(k)}
    assert {s[i : i + n] for i in range(len(s) - n + 1)} == {
        "".join(p) for p in product([str(d) for d in range(k)], repeat=n)
    }
