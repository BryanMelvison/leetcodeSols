from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # This problem is about finding the minimum cost to reach the top of a staircase, where each step has a cost associated with it. The approach I used is to create a copy of the cost list and then iterate through it, updating each step's cost to include the minimum cost of reaching that step from either of the two previous steps. Finally, I return the minimum cost of reaching either of the last two steps.
        # Time complexity: O(n) where n is the number of steps in the staircase.
        # Space complexity: O(n) for the copy of the cost list.
        # Performance:
        # Runtime: faster than 60.89%
        # Memory Usage: beats 79.14%.
        current = cost.copy()

        for idx in range(2, len(current)):
            current[idx] += min(current[idx - 1], current[idx - 2])
        


        return min(current[-1], current[-2])