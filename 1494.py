from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Kinda similar to problem 1004,  it's just a special case of k=1, with very minor modification
        # Just like the previous problem, we can use a sliding window approach to find the longest subarray with at most one zero.
        # Time complexity, O(n) : We iterate through the list once
        # Space complexity, O(1) : We use a few variables to keep track of the pointers and the count of zeros
        # Performance:
        # Runtime: faster than 63.78%
        # Memory Usage: less than 27.39%.
        first = 0
        delete = 1
        zero = 0
        maxL = 0
        for second in range(len(nums)):
            if nums[second] == 0:
                zero += 1
            
            while zero > delete:
                if nums[first] == 0:
                    zero -= 1
                first += 1
            # The reason why the length is just second-first is we omit "1" zero from the count
            maxL = max(maxL, second-first)
        return maxL