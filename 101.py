# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recursive solution, check if both nodes are None, if so return True, if one is None and the other is not, return False, if both are not None, check if their values are equal and then recursively check their left and right children.
        # Time complexity: O(n), where n is the number of nodes in the tree,
        # we visit each node once.
        # Space complexity: O(h), where h is the height of the tree, the maximum
        # depth of the recursion stack is equal to the height of the tree.
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 54.20%.
        
        def check(left, right):
            if left is None and right is None:
                return True
            
            if left is None or right is None or left.val != right.val:
                return False
            
            return check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right)
        