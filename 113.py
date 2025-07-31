# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Find all root-to-leaf paths where each path's sum equals targetSum
        # We can use a depth-first search (DFS) approach to traverse the binary tree and find all paths that sum to targetSum.
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(n) : We store n nodes on the list (stack)
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 55.46%.
        total_path = []
        if not root:
            return total_path
        # Iterative
        current = [(root, root.val, [root.val])]
        while current:
            node, val, curr = current.pop()

            if not node.left and not node.right:
                if val == targetSum:
                    total_path.append(curr)
            if node.left:
                placeholder = curr[:]
                placeholder.append(node.left.val)
                current.append((node.left, val + node.left.val, placeholder))

            if node.right:
                placeholder = curr[:]
                placeholder.append(node.right.val)
                current.append((node.right, val + node.right.val, placeholder))

        return total_path
        