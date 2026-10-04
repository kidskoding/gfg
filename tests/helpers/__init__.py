"""Test-only helpers. Topic-specific builders live in helpers.<topic>."""

import importlib


def load(name):
    """Import a numbered problem module, e.g. load("13_trees.01_height_of_binary_tree")."""
    return importlib.import_module(name)
