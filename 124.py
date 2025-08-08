# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # We can use a depth-first search (DFS) approach to traverse the binary tree and calculate the maximum path sum.
        # Here's how the algorithm works:
        # 1. We define a helper function dfs(node) that computes the maximum path sum for the subtree rooted at node.
        # 2. For each node, we recursively calculate the maximum path sums of its left and right subtrees.
        # 3. We consider two scenarios for each node:
        #    a. The maximum path sum that includes the node and both its left and right children (this is a potential candidate for the global maximum path sum).
        #    b. The maximum path sum that includes the node and either its left or right child (this is returned to the parent node for further calculations).
        # 4. We update a global variable res to keep track of the maximum path sum found so far.
        # 5. Finally, we return the value of res as the result.
        # Edge case: if the tree is empty, return 0        
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(h) : The space complexity is O(h) where h is the height of the tree
        # Performance:
        # Runtime: faster than 54.72%
        # Memory Usage: less than 80.09%.
        res = [root.val]
        def dfs(node):
            # If there's no node, the total for that should be 0
            if not node:
                return 0 
            
            # We explore like PostOrder: remember postorder:
            # left, right, root
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            # Notice we can have 2 ways of going about this: with splits and without:
            # With splits meaning, root + left + right:
            # No Splits meaning, root + max( left + right )
            # Also if value negative, make it 0, we don't count the node then:
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Then we update the max with SPLITS (assuming there's splits)
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # Then for no Splits (this helps for the DFS, say when calculating the max with splits, we need to know how deep can they go / which side to go for):
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
