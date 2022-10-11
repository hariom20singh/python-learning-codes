"""
implementation of a binary tree.
see: https://en.wikipedia.org/wiki/Binary_tree
"""
from typing import Any


class BinaryTreeNode:
    def __init__(self, data: Any = None):
        self.left = None
        self.right = None
        self.data = data
