# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # We can use a simple iterative approach to search for the value in the binary search tree (BST).
        # Since the tree is a BST, we can take advantage of the properties of BSTs
        # to navigate through the tree efficiently.
        # Time complexity: O(h), where h is the height of the tree.
        # Space complexity: O(1) for the iterative approach.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 44.91%.
        current = root
        while current:
            if val == current.val:
                return current
            elif val > current.val:
                current = current.right
            elif val < current.val:
                current = current.left
        return None
            