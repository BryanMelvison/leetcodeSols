# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:        
        # Use DFS to go through the tree, if reach a leaf node, check if the value equals targetSum, iteratively
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(n) : We store n nodes on the list (stack)
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 23.29%.
        if not root:
            return False
        
        current = [[root, root.val]]
        #Iterative approach, DFS, right then left
        while current:
            tree, value = current.pop()
            if tree.left is None and tree.right is None:
                if value == targetSum:
                    return True
            if tree.right:
                current.append([tree.right, value + tree.right.val])
            if tree.left:
                current.append([tree.left, value + tree.left.val])

        return False