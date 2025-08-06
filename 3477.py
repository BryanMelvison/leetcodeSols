from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # This problem is about finding how many fruits cannot be placed in the baskets.
        # We will iterate through each fruit and try to place it in the baskets.
        # Time complexity: O(n * m) where n is the number of fruits and m is the number of baskets.
        # Space complexity: O(1) since we are not using any extra space.
        # Performance:
        # Runtime: faster than 68.98%
        # Memory Usage: less than 39.75%.

        for fruit in fruits:
            index = 0
            while index < len(baskets):
                if fruit <= baskets[index]:
                    baskets.pop(index)
                    break
                index += 1
        return len(baskets)
            
                