# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Here is the idea:
        # We can use a depth-first search (DFS) approach to traverse the binary tree and calculate the longest ZigZag path.
        # A ZigZag path is defined as a path where the direction alternates between left and right at each step.
        # We will keep track of the length of the current ZigZag path and update the maximum length found so far.
        # We will use a recursive function to traverse the tree and calculate the longest ZigZag path.
        # The function will take three parameters: the current node, the direction (left or right), and the length of the current ZigZag path.
        # We will start the traversal from the root node and initialize the length of the ZigZag path to 0.
        # We will use a nonlocal variable to keep track of the maximum length found so far.
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(h) : The space complexity is O(h) where h is the height of the tree
        # Performance:
        # Runtime: faster than 56.26%
        # Memory Usage: less than 14.28%.
        length = 0

        def dfsMax(node, direction, steps):
            nonlocal length
            if node is None:
               return 0
            length = max(length, steps)
            if direction == "left":
                left = dfsMax(node.left, "left", 1)
                right = dfsMax(node.right, "right", steps + 1)
            elif direction == "right":
                left = dfsMax(node.left, "left", steps + 1)
                right = dfsMax(node.right, "right", 1)

        dfsMax(root.left, "left", 1)
        dfsMax(root.right, "right", 1)

        return length 

        # Much better / elegant solution (found in comment section):
        # Logic:
        # 1. We can use a depth-first search (DFS) approach to traverse the binary tree and calculate the longest ZigZag path.
        # 2. We will keep track of the length of the current ZigZag path and update the maximum length found so far.
        # 3. We will use a recursive function to traverse the tree and calculate the longest ZigZag path.
        # 4. The function will take three parameters: the current node, the length of the left ZigZag path, and the length of the right ZigZag path.
        # 5. We will start the traversal from the root node and initialize the lengths of the left and right ZigZag paths to 0.
        # 6. We will use a nonlocal variable to keep track of the maximum length found so far.
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(h) : The space complexity is O(h) where h is the height of the tree
        # best = 0
        # def dfs(node, left, right):
        #     nonlocal best
        #     best = max(best, left, right)

        #     if node.left:
        #         dfs(node.left, right + 1, 0)
        #     if node.right:
        #         dfs(node.right, 0, left + 1)
            
        
        # dfs(root, 0, 0)
        # return best