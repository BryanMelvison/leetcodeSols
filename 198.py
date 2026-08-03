from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # This problem is about finding the maximum amount of money that can be robbed from a list of houses, where adjacent houses cannot be robbed. The approach I used is to create a copy of the list and then iterate through it, updating each house's value to include the maximum amount that can be robbed from either of the two previous houses. Finally, I return the maximum amount that can be robbed from either of the last two houses.
        # Time complexity: O(n) where n is the number of houses.
        # Space complexity: O(n) for the copy of the list.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: beats 60.98%.
        result = nums[:]
        for idx in range(2, len(nums)):
            if idx - 2 == 0:
                result[idx] += result[idx - 2]
            else:
                result[idx] += max(result[idx - 2], result[idx - 3])
        return max(result)
