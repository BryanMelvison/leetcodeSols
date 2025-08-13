# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # We use a breadth-first search (BFS) approach to traverse the binary tree level by level to perform Level Order Traversal.
        # For each level, we calculate the sum of the node values and keep track of the maximum sum encountered.
        # The level with the maximum sum is returned as the result.
        # Time complexity: O(n), where n is the number of nodes in the tree.
        # Space complexity: O(n) for the queue used in BFS.
        # Performance: 
        # Runtime: faster than 46.86%
        # Memory Usage: less than 77.04%.
        maxSum = float("-inf")

        from collections import deque

        queue = deque([root])
        level = 0
        maxLevel = 0
        while queue:
            level += 1
            current_level = len(queue)
            currSum = 0
            for i in range(current_level):
                curr = queue.popleft()
                currSum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            
            if currSum > maxSum:
                maxSum = currSum
                maxLevel = level
        
        return maxLevel
            

        