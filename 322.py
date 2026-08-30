from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # assume coin is sorted, for this, I need to first instantiate a map of current with base case, 
        # then I build up the map from 1,,, amount, then I iterate over all the coins, and find the best possible combination
        # Time complexity: O(n * m), where n is the amount and m is the number of coins, we visit each amount for each coin.
        # Space complexity: O(n), we are using a map to store the minimum number of
        # coins needed to make change for each amount.
        # Performance:
        # Runtime: faster than 31.77%.
        # Memory Usage: less than 32.88%.
        current_map = {0 : 0}
        for idx in range(1, amount + 1):
            current_min = amount + 1 
            for coin in coins:
                if coin > idx:
                    continue
                remainder = idx - coin
                if remainder in current_map:
                    candidate  = 1 + current_map[remainder]
                    current_min = min(candidate, current_min)
            current_map[idx] = current_min
        return current_map[amount] if current_map[amount] <= amount else -1        

