from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # We can just keep track of the current altitude and the maximum altitude.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 96.81%.
        max_height = 0
        current = 0
        for i in gain:
            current += i
            if current > max_height:
                max_height = current
        return max_height