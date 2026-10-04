# gfg

gfg data structures and algorithms problems for coding interviews!

Source: [GeeksforGeeks — Must Do Coding Questions for Companies like Amazon, Microsoft, Adobe](https://www.geeksforgeeks.org/dsa/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/)

Each `src/<topic>/README.md` lists that topic's problems.

## Running tests

```
uv run pytest                                   # everything
nix run .                                       # same, via the flake (optional)
uv run pytest tests/01_arrays                   # one topic
uv run pytest tests/13_trees/test_01_height_of_binary_tree.py   # one problem
```

Each topic is a package numbered in study order: `src/NN_<topic>/NN_<slug>.py` holds the stub,
`tests/NN_<topic>/test_NN_<slug>.py` its tests.
Stubs `raise NotImplementedError` until solved.

`tests/helpers/__init__.py` has `load("NN_<topic>.NN_<slug>")`. Topic builders live in `tests/helpers/<topic>.py`
(e.g. `helpers.trees.build([...])`: level-order list, `None` = missing node; `to_list(root)` for writing cases).
Node classes live in `src/core/`, one per file (e.g. `from core.tree_node import TreeNode`), since a numbered
package can't appear in an `import` statement.
