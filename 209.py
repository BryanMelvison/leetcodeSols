from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # This problem is about finding the minimum length of a contiguous subarray of which the sum is greater than or equal to a given target. The approach I used is a two-pointer technique, where we maintain a sliding window of elements and adjust the window size based on the current sum compared to the target.
        # Time complexity: O(n) where n is the number of elements in the list,
        # since we are iterating through the list once with the right pointer and adjusting the left pointer as needed.
        # Space complexity: O(1) since we are using a constant amount of space for
        # variables and not storing any additional data structures.
        # Performance:
        # Runtime: faster than 78.74%
        # Memory Usage: beats 16.43%.
        minimum_length = 1000000
        local_sum = 0

        # 2 pointer
        left = 0
        for right in range(len(nums)):
            local_sum += nums[right]
            while local_sum >= target:
                minimum_length = min(minimum_length, right - left + 1)
                local_sum -= nums[left]
                left += 1
        return minimum_length if minimum_length != 1000000 else 0