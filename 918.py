from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Can just use Kadane's Algorithm to calculate the normal max subarray, and then
        # compare it with global minimum sum, to see if it counts, 
        # Time complexity: O(n) where n is the number of elements in the list.
        # Space complexity: O(1) since we are using a constant amount of space.
        # Performance:
        # Runtime: faster than 92.46%
        # Memory Usage: beats 87.79%
        if max(nums) < 0:
            return max(nums)

        max_sum = float("-inf")
        current_max_sum = 0

        current_min_sum = 0
        min_sum = float("inf")
        for num in nums:
            current_max_sum += num
            current_max_sum = max(current_max_sum, num)

            max_sum = max(current_max_sum, max_sum)

            current_min_sum += num
            current_min_sum = min(current_min_sum, num)

            min_sum = min(current_min_sum, min_sum)
    
        min_min_sum = sum(nums) - min_sum
        return max(max_sum, min_min_sum)