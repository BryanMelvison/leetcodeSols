# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Find the number of paths that sum to targetSum
        # We can use a depth-first search (DFS) approach to traverse the binary tree and count the number of paths that sum to targetSum.
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(n) : We store n nodes on the list (stack)
        # Performance:
        # Runtime: faster than 64.64%
        # Memory Usage: less than 33.39%.
        # Remember 2 sum, and solving
        prefix = {0 : 1} # Base case If root node == targetSum:

        def dfs(node, currSum):
            if node is None:
                return 0
            
            currSum += node.val
            # CUz we check initially, in the stack, since this is DFS, we go through left, left, left, the stack goes like this (for example 1:
            # 10, 5 , 3, 3, -2, 2, 1, -3, 11
            # ITs quite similar to 2 sum remember that

            currentTotal = prefix.get(currSum - targetSum, 0)
            prefix[currSum] = prefix.get(currSum, 0) + 1

            currentTotal += dfs(node.left, currSum)
            currentTotal += dfs(node.right, currSum)

            # Backtrack, so other nodes don't get info from diff branches
            prefix[currSum] -= 1

            return currentTotal
        
        return dfs(root, 0)
