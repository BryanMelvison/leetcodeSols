# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Just perform a level order traversal and keep track of the last node at each level.
        # Time complexity: O(n), where n is the number of nodes in the tree.
        # Space complexity: O(n) for the queue used in BFS.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 60.66%.
        import collections

        # BFS with levels:
        queue = collections.deque([root])
        result = []
        level_size = 1 

        while queue:
            curr = None
            for i in range(level_size):
                curr = queue.popleft()
                if curr is not None:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            if curr is not None:
                result.append(curr.val)
            level_size = len(queue)

        return result