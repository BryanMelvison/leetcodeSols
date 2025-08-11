# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Iterative (my approach):
        # What I did was basically, take note of the parent-child relationship in a dictionary, then from it, I go bottom up approach to take note of the parents of each node, and then I find the first similar node across both tracked nodes, its O(n) but it also is O(n) space complexity
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(n) : We store n nodes in the family_node and val_node dictionaries
        # Performance:  
        # Runtime: faster than 57.89%
        # Memory Usage: less than 5.61%.

        # family_node = {}
        # val_node = {root.val: root}
        # def dfs(node, parent):
        #     if not node:
        #         return 0
        #     if parent != None:
        #         family_node[node.val] = parent
        #         val_node[node.val] = node

        #     if node.left:
        #         dfs(node.left, node.val)
            
        #     if node.right:
        #         dfs(node.right, node.val)
        
        # dfs(root, None)

        # def tracker(node):
        #     # Now check for similarity:
        #     visited = []
        #     current = node.val
        #     while True:
        #         if current not in family_node:
        #             visited.append(current)
        #             break
                
        #         visited.append(current)

        #         nextOne = family_node[current]
        #         current = nextOne
        #     return visited

        # q_track = set(tracker(q))
        # p_track = tracker(p)

        # for track in p_track:
        #     if track in q_track:
        #         return val_node[track]        
        # return None

        # Recursive (Classic Solution)
        # The idea is to traverse the tree recursively, and check if the current node is either p or q. If it is, we return that node. If we find both p and q in the left and right subtrees, then the current node is the lowest common ancestor.
        # Time complexity, O(n) : We traverse each node once
        # Space complexity, O(h) : The space complexity is O(h) where h is the height of the tree (due to recursion stack)
        # Performance:
        # Runtime: faster than 63.73%
        # Memory Usage: less than 87.28%.
        def dfs(node):
            # Base case
            if node is None:
                return
            if node == p or node == q:
                return node
            #   dfs(3)
            #   dfs(5)
            #     dfs(6)    -> left/right None, node!=p/q -> return None
            #     dfs(2)
            #       dfs(7)  -> return None
            #       dfs(4)  -> return None
            #       (2 sees left=None right=None and 2!=p/q) -> return None
            #     (5: check node==p? yes -> return Node(5))
            #   dfs(1)
            #     dfs(0) -> None
            #     dfs(8) -> None
            #     (1: node==q? yes -> return Node(1))
            #   (3: left returned Node(5), right returned Node(1) -> both non-None)
            #   -> dfs(3) returns Node(3)  ← this is the LCA
            # Post Order that bubbles up the answer
            # For first example(once it goes through left branch, it returns 5 as it is one of the target nodes, then same goes for right)
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            else:
                # Bottom part here is critical, especially for cases  where the ancestor resides in the same branch(need to try drawing it out, lay out the recursion tree for easier visualization)
                if left:
                    return left
                if right:
                    return right
            
        return dfs(root)
            