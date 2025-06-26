from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort the costs in descending order and buy two items at a time, skipping every third item.
        # Time complexity, O(n log n) : sorting the list
        # Space complexity, O(1) : we are not using any extra space except for the variables
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 13%. 
        min_cost = 0
        current_bought = 0
        cost.sort(reverse=True)
        for price in cost:
            if current_bought != 2:
                min_cost += price
                current_bought += 1
            else:
                current_bought = 0
                continue
        return min_cost