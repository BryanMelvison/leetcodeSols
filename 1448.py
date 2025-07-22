# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # We can use a depth-first search (DFS) approach to traverse the binary tree and count the number of "good" nodes.
        # A "good" node is defined as a node whose value is greater than or equal to the maximum value encountered on the path from the root to that node.
        # Time complexity, O(n) : We traverse each node once    
        # Space complexity, O(h) : The space complexity is O(h) where h is the height of the tree 
        # Performance:
        # Runtime: faster than 45.78%
        # Memory Usage: less than 81.70%.
        
        def dfsTraversal(node, maxValue):
            if not node:
                return 0
            if node.val >= maxValue:
                return dfsTraversal(node.left, node.val) + dfsTraversal(node.right, node.val) + 1
            else:
                return dfsTraversal(node.left, maxValue) + dfsTraversal(node.right, maxValue) 

        return dfsTraversal(root, float('-inf'))