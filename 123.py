from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Prefix and Suffix sum,
        # count trade from [0: k] and [k+1:n]
        # to keep track we need to look ahead
        # Time complexity: O(n), where n is the length of the prices list, we
        # visit each element once.
        # Space complexity: O(n), we are using a list to store the prefix and suffix
        # Performance:
        # Runtime: faster than 65.44%.
        # Memory Usage: less than 41.09%.
        left = [0]
        minimumPrice = prices[0]
        maxprofit = 0
        for idx in range(1, len(prices)):
            if prices[idx] > minimumPrice:
                maxprofit = max(maxprofit, prices[idx] - minimumPrice)
            else:
                minimumPrice = prices[idx]
            left.append(maxprofit)
        right = []
        maximumPrice = prices[-1]
        maxprofit = 0
        for idx in range(len(prices) -1 , -1, -1):
            if prices[idx] < maximumPrice:
                maxprofit = max(maxprofit, maximumPrice-prices[idx])
            else:
                maximumPrice = prices[idx]
            right.append(maxprofit)

        maxim = 0
        for l, r in zip(left, right[::-1]):
            if l + r > maxim:
                maxim = l+r
        return maxim
