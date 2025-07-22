from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Iterative DFS, add leafNodes, and compare each
        # Time complexity, O(n) : We traverse each node once    
        # Space complexity, O(n) : The space complexity is O(n) where n is the node appended to the array for DFS (iterative approach)
        # Performance:
        # Runtime: faster than 100.00%
        # Memory Usage: less than 43.97%.

        def leafNode(root):
            leafNodes = []

            explore = [root]

            while explore:
                current = explore.pop()

                if not current.left and not current.right:
                    leafNodes.append(current.val)
                
                # Since pop last, so left is added after
                if current.right:
                    explore.append(current.right)
                
                if current.left:
                    explore.append(current.left)
            return leafNodes
        
        leafNode1 = leafNode(root1)
        leafNode2 = leafNode(root2)

        return leafNode1 == leafNode2
                