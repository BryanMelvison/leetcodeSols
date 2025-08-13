# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Perform a level order traversal of the binary tree and return the values at each level.
        # We can use a queue to keep track of the nodes at each level.
        # Time complexity: O(n), where n is the number of nodes in the tree.
        # Space complexity: O(n) for the queue used in BFS.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 38.64%.
        if not root:
            return []
        from collections import deque
        result = []
        queue = deque([root])
        while queue:
            level = len(queue)
            curr_level = []
            for i in range(level):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(curr_level)
        return result