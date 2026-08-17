from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the smallest number we have seen so far and the maximum profit we can make by selling at the current price.
        # Time complexity: O(n), where n is the length of the prices list, we
        # visit each element once.
        # Space complexity: O(1), we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 65.44%.
        # Memory Usage: less than 41.09%.

        maxProfit = 0
        smallest_num = prices[0]
        for idx in range(1, len(prices)):
            if prices[idx] > smallest_num:
                maxProfit = max(maxProfit, prices[idx] - smallest_num)
            elif smallest_num > prices[idx]:
                smallest_num = prices[idx]
        
        return maxProfit