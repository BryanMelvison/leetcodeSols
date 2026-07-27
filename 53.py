from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This problem is about finding the maximum sum of a contiguous subarray in a given list of integers. The approach I used is to iterate through the list, keeping track of the current total and the final maximum found so far. If the current total becomes less than the current number, I reset the current total to the current number. At the end of the iteration, I return the final maximum found.
        # Time complexity: O(n) where n is the number of elements in the list.
        # Space complexity: O(1) since we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 65.63%
        # Memory Usage: beats 73.68%.
        final_max = float('-inf')
        current_total = 0
        for num in nums:
            current_total += num
            current_total = max(num, current_total)

            final_max = max(current_total, final_max)
        return final_max
        
