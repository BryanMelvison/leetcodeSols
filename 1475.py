from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # So for this problem, I used a stack to keep track of the prices and the total number of days that the price was less than or equal to the current price. For each price, we pop from the stack until we find a price that is greater than the current price, and we add the total number of days that we popped to the total number of days for the current price.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the stack
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 93.45%.
        # Monotonic stack
        result = prices[:]
        stack = []
        for idx in range(len(prices)):
            while len(stack) != 0 and prices[stack[-1]] >= prices[idx]:
                current = stack.pop(-1)
                result[current] = prices[current] - prices[idx]

            stack.append(idx)
        return result