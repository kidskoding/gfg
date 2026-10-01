# gfg

gfg data structures and algorithms problems for coding interviews!

Source: [GeeksforGeeks — Must Do Coding Questions for Companies like Amazon, Microsoft, Adobe](https://www.geeksforgeeks.org/dsa/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/)

Each `src/<topic>/README.md` lists that topic's problems.

## Running tests

```
pytest                                          # everything (inside nix develop / direnv)
nix run .                                       # same, via the flake (optional)
pytest tests/arrays                             # one topic
pytest tests/trees/test_01_height_of_binary_tree.py   # one problem
```

Each topic is a package: `src/<topic>/NN_<slug>.py` holds the stub, `tests/<topic>/test_NN_<slug>.py` its tests.
Stubs `raise NotImplementedError` until solved.

`tests/helpers/__init__.py` has `load("<topic>.NN_<slug>")`. Topic builders live in `tests/helpers/<topic>.py`
(e.g. `helpers.trees.build([...])`: level-order list, `None` = missing node; `to_list(root)` for writing cases).
`src/trees/tree.py` holds `TreeNode`.
