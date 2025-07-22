from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive approach (Depth-First Search)
        # We can use a recursive approach to find the maximum depth of the binary tree.
        # Time complexity, O(n) : We traverse each node once    
        # Space complexity, O(h) : The space complexity is O(h) where h is the height of the tree due to recursion stack
        # Performance:
        # Runtime: faster than 100.00%
        # Memory Usage: less than 47.74%.
        if not root:
            return 0
        def traverse(node):
            if not node.left and not node.right:
                return 1
            if node.left and not node.right:
                return traverse(node.left) + 1
            elif node.right and not node.left:
                return traverse(node.right) + 1
            else:
                return max(traverse(node.left), traverse(node.right)) + 1

        return traverse(root)        