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
        minimum_price = prices[0]
        total_profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > minimum_price:
                total_profit += prices[idx] - minimum_price

            minimum_price = prices[idx]
        return total_profit